# Monorepo & Naming Conventions

## Monorepo validation

Le dépôt est structuré en mono-repo avec deux applications principales :

- `backend/` : API Django REST Framework, logique métier, modèles, serializers, viewsets
- `frontend/` : application React, pages, composants, hooks, clients API

Cette séparation respecte le cahier des charges demandé pour le test technique SMARTHOLOL.

## Why this structure

- Isolation claire des responsabilités backend/frontend
- Setup indépendant par dossier
- Documentation locale par application
- Évolution possible vers CI séparée ou jobs ciblés

## Naming conventions

### Backend
- Fichiers Python : `snake_case.py`
- Fonctions/méthodes : `snake_case`
- Classes : `PascalCase`
- Variables de configuration : `UPPER_SNAKE_CASE`
- Routes API : noms REST explicites et pluriels quand nécessaire

### Frontend
- Composants React : `PascalCase.jsx`
- Hooks : `useSomething.js`
- Modules API : `camelCase` descriptif (`medicamentsApi.js`)
- Pages : `PascalCase` avec suffixe `Page`
- Utilitaires : fonctions courtes et nommées explicitement

## Current validated structure

- `backend/config/` for Django configuration
- `backend/apps/` for domain apps
- `frontend/src/api/` for HTTP access layer
- `frontend/src/components/` for reusable UI
- `frontend/src/pages/` for page-level composition
- `frontend/src/hooks/` for reusable logic
