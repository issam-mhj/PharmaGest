"""Business services for sale creation and cancellation workflows."""
from decimal import Decimal

from django.db import transaction
from rest_framework import serializers

from apps.medicaments.models import Medicament

from .models import LigneVente, Vente


@transaction.atomic
def create_vente_with_stock_deduction(*, notes=None, lignes_data=None) -> Vente:
    """Create a sale, store line snapshots, and deduct stock atomically."""
    lignes_data = lignes_data or []
    if not lignes_data:
        raise serializers.ValidationError({"lignes": "La vente doit contenir au moins une ligne."})

    vente = Vente.objects.create(notes=notes or "", statut=Vente.Statut.COMPLETEE, est_active=True)
    total = Decimal("0.00")

    for item in lignes_data:
        medicament_id = item["medicament"].id if hasattr(item["medicament"], "id") else item["medicament"]
        quantite = item["quantite"]

        if quantite <= 0:
            raise serializers.ValidationError({"quantite": "La quantité doit être strictement positive."})

        medicament = (
            Medicament.objects.select_for_update()
            .filter(pk=medicament_id, est_actif=True)
            .first()
        )
        if medicament is None:
            raise serializers.ValidationError(
                {"medicament": f"Le médicament #{medicament_id} est introuvable ou inactif."}
            )

        if medicament.stock_actuel < quantite:
            raise serializers.ValidationError(
                {
                    "stock": (
                        f"Stock insuffisant pour {medicament.nom}. "
                        f"Disponible: {medicament.stock_actuel}, demandé: {quantite}."
                    )
                }
            )

        prix_unitaire = medicament.prix_vente
        ligne = LigneVente.objects.create(
            vente=vente,
            medicament=medicament,
            quantite=quantite,
            prix_unitaire=prix_unitaire,
        )
        total += ligne.sous_total

        medicament.stock_actuel -= quantite
        medicament.save(update_fields=["stock_actuel"])

    vente.total_ttc = total
    vente.save(update_fields=["total_ttc"])
    return vente


@transaction.atomic
def cancel_vente_and_restore_stock(vente: Vente) -> Vente:
    """Cancel a sale and restore stock for all related lines atomically."""
    if vente.statut == Vente.Statut.ANNULEE:
        raise serializers.ValidationError({"statut": "Cette vente est déjà annulée."})

    lignes = vente.lignes.select_related("medicament").all()
    for ligne in lignes:
        medicament = Medicament.objects.select_for_update().get(pk=ligne.medicament_id)
        medicament.stock_actuel += ligne.quantite
        medicament.save(update_fields=["stock_actuel"])

    vente.statut = Vente.Statut.ANNULEE
    vente.est_active = False
    vente.save(update_fields=["statut", "est_active"])
    return vente