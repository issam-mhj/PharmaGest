# Contribution Guide

Ce projet suit les standards SMARTHOLOL pour un mono-repo full-stack contenant un backend Django et un frontend React.

## Workflow Git

- Branche principale protégée : `main`
- Branche d'intégration optionnelle : `develop`
- Branches de travail recommandées :
  - `feat/<scope>`
  - `fix/<scope>`
  - `docs/<scope>`
  - `refactor/<scope>`
  - `chore/<scope>`

Exemples :
- `feat/medicaments-crud`
- `fix/vente-annulation-stock`
- `docs/swagger-readme`

## Conventional Commits

Tous les commits doivent suivre le format suivant :

```text
<type>(<scope>): <description>
```

Le `scope` est recommandé mais non obligatoire.

### Types autorisés

- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: documentation
- `refactor`: refactorisation sans changement fonctionnel
- `test`: ajout ou modification de tests
- `chore`: maintenance, config, dépendances
- `build`: changements liés au build ou packaging
- `ci`: intégration continue

### Exemples valides

- `feat(categories): add category viewset`
- `feat(ventes): create stock deduction service`
- `fix(medicaments): prevent negative stock`
- `docs(readme): add local setup instructions`
- `refactor(frontend): extract sales form hook`
- `chore(repo): add github review templates`

### Règles de rédaction

- Utiliser l'anglais pour les messages de commit.
- Commencer la description par un verbe à l'infinitif implicite.
- Garder une description courte, claire et atomique.
- Éviter les commits massifs mélangeant backend, frontend et documentation sans lien.

## Politique de Pull Request

- Une Pull Request doit traiter un seul sujet métier ou technique.
- Une Pull Request doit être relue avant merge.
- Une Pull Request doit inclure le contexte, les changements effectués et les points à vérifier.
- Toute PR impactant l'API doit mentionner les endpoints concernés.
- Toute PR impactant l'UI doit inclure captures d'écran si pertinent.

## Structure du mono-repo

- `backend/` : projet Django REST Framework
- `frontend/` : application React
- `docs/` : conventions, stratégie de review, architecture

## Conventions de nommage

### Python / Django

- Variables et fonctions : `snake_case`
- Classes : `PascalCase`
- Constantes : `UPPER_SNAKE_CASE`
- Modules/fichiers : `snake_case.py`
- Applications Django : noms courts et explicites au pluriel si métier (`categories`, `medicaments`, `ventes`)

### React

- Composants : `PascalCase`
- Hooks : `camelCase` préfixé par `use`
- Fonctions utilitaires : `camelCase`
- Dossiers de composants métier : noms explicites (`medicaments`, `ventes`)
- Pages : suffixe `Page` (`DashboardPage`, `MedicamentsPage`)

## Règle d'or

Si un changement nécessite une longue explication dans le commit, il est probablement trop gros et doit être découpé.
