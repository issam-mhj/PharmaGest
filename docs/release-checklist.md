# Checklist de Validation Finale

Cette checklist est prévue pour la phase de livraison finale.

## Backend

- [ ] `python manage.py migrate` exécuté sans erreur
- [ ] `python manage.py loaddata fixtures/initial_data.json` exécuté
- [ ] Swagger accessible sur `/api/schema/swagger-ui/`
- [ ] Endpoints CRUD Catégories OK
- [ ] Endpoints CRUD Médicaments + `/alertes/` OK
- [ ] Endpoints Ventes + `/annuler/` OK
- [ ] Déduction/réintégration stock vérifiées
- [ ] `python manage.py test` passe

## Frontend

- [ ] `npm install` puis `npm run dev` sans erreur
- [ ] Dashboard affiche les 3 KPI
- [ ] Module Médicaments: liste, filtres, pagination, création, édition, archivage
- [ ] Module Ventes: multi-lignes, total live, historique, détail, annulation
- [ ] Gestion erreurs/loading visible et compréhensible

## Configuration

- [ ] `.env.example` backend/frontend à jour et sans secrets
- [ ] `.gitignore` backend/frontend vérifiés
- [ ] README racine + backend + frontend cohérents

## Git & livraison

- [ ] Historique lisible en Conventional Commits
- [ ] Minimum 15 commits atomiques
- [ ] Dernière revue des fichiers modifiés
- [ ] Dépôt poussé vers remote (GitHub/GitLab)
