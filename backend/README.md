# Pharma Backend

Backend Django REST Framework pour le projet PharmaManager.

## Démarrage rapide

1. `python -m venv venv`
2. `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
3. `pip install -r requirements.txt`
4. Copier `.env.example` vers `.env`
5. `python manage.py migrate`
6. `python manage.py loaddata fixtures/initial_data.json`
7. `python manage.py runserver`

## Fondation Django en place

- Settings modulaires : `config/settings/base.py` et `config/settings/local.py`
- Settings de production prêts : `config/settings/production.py`
- Base de données PostgreSQL configurée via variables d'environnement
- DRF + drf-spectacular configurés pour Swagger
- Pagination, filtres et tri globaux configurés dans `REST_FRAMEWORK`
- CORS et paramètres de sécurité pilotés par `.env`
- Gestion standardisée des erreurs API via un exception handler central

## Variables d'environnement principales

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `CORS_ALLOWED_ORIGINS`
- `CSRF_TRUSTED_ORIGINS`
- `PAGINATION_PAGE_SIZE`
- `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`

## Endpoints clés

- `GET /api/v1/categories/` : liste des catégories
- `POST /api/v1/categories/` : création catégorie
- `GET /api/v1/medicaments/` : liste paginée des médicaments actifs
- `GET /api/v1/medicaments/alertes/` : médicaments en alerte stock bas
- `POST /api/v1/ventes/` : création vente avec lignes
- `POST /api/v1/ventes/{id}/annuler/` : annulation vente + réintégration stock

Documentation Swagger : `http://localhost:8000/api/schema/swagger-ui/`

## Qualité backend

- Tests unitaires/API disponibles dans `apps/*/tests/`
- Fixture de démo disponible dans `fixtures/initial_data.json`
- Script de vérification locale:
	- PowerShell: `scripts/verify_local.ps1`
	- Bash: `scripts/verify_local.sh`

## Cas métier à vérifier rapidement

1. Créer une catégorie
2. Créer un médicament avec stock faible
3. Vérifier qu'il apparaît dans `/api/v1/medicaments/alertes/`
4. Créer une vente sur ce médicament
5. Vérifier la déduction du stock
6. Annuler la vente
7. Vérifier la réintégration du stock
