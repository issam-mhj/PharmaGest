# TODO Global — PharmaManager

## 0) Gouvernance & setup initial
- [x] Initialiser le dépôt Git avec convention Conventional Commits.
- [x] Ajouter protections de branches et stratégie de revue de code.
- [x] Valider la structure mono-repo avec `backend/` et `frontend/`.
- [x] Définir conventions de nommage (Python snake_case, React PascalCase).

## 1) Backend — Fondation Django
- [x] Créer le projet Django avec settings modulaires (`base.py`, `local.py`).
- [x] Configurer PostgreSQL via variables d'environnement.
- [x] Configurer DRF et drf-spectacular.
- [x] Ajouter CORS et paramètres de sécurité dev/prod.
- [x] Mettre en place pagination, filtres et gestion d'erreurs standard.

## 2) Backend — App `categories`
- [x] Modèle `Categorie` (nom unique, description optionnelle, timestamps).
- [x] Serializer avec validations métier.
- [x] ViewSet CRUD complet + permissions adaptées.
- [x] Routes versionnées `/api/v1/categories/`.
- [x] Documentation Swagger complète (tags, exemples, erreurs).

## 3) Backend — App `medicaments`
- [x] Modèle `Medicament` avec tous les champs demandés.
- [x] Implémenter soft delete (`est_actif=False`).
- [x] Ajouter propriété `est_en_alerte`.
- [x] Serializer avec validations (prix, stock, dates).
- [x] ViewSet CRUD + recherche + filtres (catégorie, stock, expiration).
- [x] Endpoint `/api/v1/medicaments/alertes/`.
- [x] Swagger détaillé pour tous les endpoints.

## 4) Backend — App `ventes`
- [x] Modèle `Vente` (référence auto-générée, statut, total, notes).
- [x] Modèle `LigneVente` avec snapshot `prix_unitaire`.
- [x] Service métier transactionnel création vente + déduction stock.
- [x] Endpoint annulation vente + réintégration stock.
- [x] Historique des ventes avec filtres date/statut.
- [x] Swagger complet, y compris erreurs stock insuffisant.

## 5) Backend — Qualité
- [x] Ajouter docstrings sur modèles, serializers et viewsets.
- [x] Mettre en place tests unitaires (models, serializers, API).
- [x] Ajouter fixtures/seeds (catégories, médicaments de démo).
- [x] Vérifier codes HTTP et messages d'erreur cohérents.
- [x] Préparer script de vérification locale (lint + tests).

## 6) Frontend — Fondation React (Vite)
- [x] Initialiser l'app React et la structure `src/`.
- [x] Configurer Axios (`api/axiosConfig.js`) avec `VITE_API_BASE_URL`.
- [x] Mettre en place React Query pour cache/requêtes.
- [x] Créer layout global + navigation (Dashboard, Médicaments, Ventes).
- [x] Ajouter gestion globale loading/error.

## 7) Frontend — Module Médicaments
- [x] Page liste avec recherche, filtres, pagination.
- [x] Afficher indicateurs visuels de stock bas.
- [x] Formulaire création/modification médicament.
- [x] Action archivage (soft delete côté API).
- [x] Hooks dédiés (`useMedicaments`, mutations CRUD).

## 8) Frontend — Module Ventes
- [x] Formulaire de vente multi-lignes (médicament + quantité).
- [x] Calcul du total en temps réel côté UI.
- [x] Validation utilisateur (quantités, stock disponible).
- [x] Liste historique des ventes + détails.
- [x] Action d'annulation de vente avec confirmation.

## 9) Frontend — Dashboard
- [x] KPI: nombre total de médicaments actifs.
- [x] KPI: alertes de stock bas.
- [x] KPI: ventes du jour.
- [x] Widgets simples et lisibles.

## 10) Documentation & DX
- [x] Compléter README racine (setup < 10 min).
- [x] Compléter `backend/README.md` et `frontend/README.md`.
- [x] Ajouter `.env.example` exhaustifs sans secrets.
- [x] Documenter endpoints clés et scénarios métier.

## 11) Git & livraison
- [x] Produire au moins 15 commits conventionnels atomiques.
- [x] Vérifier `.gitignore` backend/frontend.
- [x] Ajouter checklist de validation finale.
- [x] Préparer démonstration fonctionnelle (Swagger + UI)

## 12) Bonus (optionnel)
- [x] JWT auth (`simplejwt`).
- [ ] Filtres avancés (`django-filter`).
- [ ] Export CSV (inventaire/ventes).
- [ ] Docker Compose full stack.
- [x] CI (lint, tests) sur push/PR.

---

## Ordre recommandé d'exécution
1. Backend models + migrations
2. API CRUD + logique stock
3. Swagger
4. Frontend pages principales
5. Tests + documentation
6. Hardening + bonus
