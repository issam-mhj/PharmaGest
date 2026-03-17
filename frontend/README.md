# Pharma Frontend

Frontend React (Vite) pour PharmaManager.

## Démarrage rapide

1. `npm install`
2. Copier `.env.example` vers `.env`
3. `npm run dev`

## Fondation en place

- Bootstrap Vite + React (`index.html`, `src/main.jsx`)
- Routing global (`Dashboard`, `Médicaments`, `Ventes`)
- Axios configuré via `VITE_API_BASE_URL`
- React Query configuré pour requêtes/caching
- Gestion globale loading/error via `GlobalRequestStatus`

## Modules livrés

- Dashboard : KPIs + widgets alertes/ventes récentes
- Médicaments : liste, filtres, pagination, création/édition, archivage
- Ventes : formulaire multi-lignes, total live, historique, détail, annulation

## Variables d'environnement

- `VITE_API_BASE_URL` : URL de base de l'API backend
- `VITE_APP_NAME` : nom affiché de l'application (optionnel)
