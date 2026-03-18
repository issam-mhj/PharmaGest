# PharmaManager (PharmaGest)

Application de gestion de pharmacie (MVP) selon les standards SMARTHOLOL.

## Structure du projet

- backend/ : API Django REST Framework + PostgreSQL + Swagger
- frontend/ : Interface React (Vite) avec couche API dédiée

## Stack

- Backend : Python, Django, DRF, drf-spectacular, PostgreSQL
- Frontend : React.js (Vite), Axios, React Query

## Installation rapide (moins de 10 minutes)

### Backend

1. Aller dans `backend`
2. Créer et activer un environnement virtuel
3. Installer les dépendances via `requirements.txt`
4. Copier `.env.example` vers `.env` et adapter PostgreSQL
5. Exécuter les migrations et charger les données de démo
6. Lancer le serveur Django

### Frontend

1. Aller dans `frontend`
2. Installer les dépendances npm
3. Copier `.env.example` vers `.env`
4. Lancer l'application React

## Commandes de démarrage (Windows PowerShell)

### Backend

1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `copy .env.example .env`
6. `python manage.py migrate`
7. `python manage.py loaddata fixtures/initial_data.json`
8. `python manage.py runserver`

### Frontend

1. `cd frontend`
2. `npm install`
3. `copy .env.example .env`
4. `npm run dev`

## Documentation API

- Swagger UI : `http://localhost:8000/api/schema/swagger-ui/`
- Détails endpoints + scénarios : [docs/api-endpoints.md](docs/api-endpoints.md)

## Bonus implémentés

- JWT auth (SimpleJWT) :
	- `POST /api/v1/auth/token/`
	- `POST /api/v1/auth/token/refresh/`
	- `GET /api/v1/auth/me/` (protégé)
- CI GitHub Actions : [workflow CI](.github/workflows/ci.yml)

## Plan global

Le plan d'exécution détaillé du projet se trouve dans [PROJECT_TODO.md](PROJECT_TODO.md).

## Gouvernance du dépôt

- Guide de contribution : [CONTRIBUTING.md](CONTRIBUTING.md)
- Stratégie de protection des branches : [docs/branch-protection.md](docs/branch-protection.md)
- Conventions mono-repo et nommage : [docs/monorepo-conventions.md](docs/monorepo-conventions.md)

## Vérification qualité

- Backend : `backend/scripts/verify_local.ps1`
- Tests Django : `python manage.py test`