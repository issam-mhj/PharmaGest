# Script de Démonstration Fonctionnelle (Swagger + UI)

Durée cible: 8 à 12 minutes.

## 1) Préparation (2 min)

1. Lancer backend (`python manage.py runserver`)
2. Lancer frontend (`npm run dev`)
3. Ouvrir Swagger et l'application frontend

## 2) Démonstration API via Swagger (3 à 4 min)

### Catégories
- Créer une catégorie
- Lister les catégories

### Médicaments
- Créer un médicament
- Lister les médicaments
- Vérifier endpoint `GET /api/v1/medicaments/alertes/`
- Archiver un médicament (soft delete)

### Ventes
- Créer une vente multi-lignes
- Vérifier total + lignes
- Annuler une vente via `/api/v1/ventes/{id}/annuler/`
- Vérifier changement de statut

## 3) Démonstration UI (3 à 4 min)

### Dashboard
- Montrer KPI médicaments actifs
- Montrer KPI alertes stock bas
- Montrer KPI ventes du jour

### Médicaments
- Recherche/filtres/pagination
- Création + modification
- Archivage avec confirmation

### Ventes
- Formulaire multi-lignes
- Calcul total temps réel
- Validation stock insuffisant
- Historique + détail + annulation

## 4) Qualité & DX (1 min)

- Montrer structure mono-repo `backend/` + `frontend/`
- Montrer docs (`README`, `docs/api-endpoints.md`, `docs/release-checklist.md`)
- Montrer scripts de vérification backend (`scripts/verify_local.ps1`)

## 5) Clôture

- Rappeler que l'historique Git suit Conventional Commits
- Confirmer disponibilité de la documentation d'installation
