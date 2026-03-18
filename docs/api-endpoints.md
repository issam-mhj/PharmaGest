# API Endpoints & Scénarios Métier

Ce document résume les endpoints principaux et les scénarios fonctionnels à tester.

## Base URL

- API v1 : `/api/v1/`
- Swagger : `/api/schema/swagger-ui/`

## Catégories

- `GET /api/v1/categories/`
- `POST /api/v1/categories/`
- `GET /api/v1/categories/{id}/`
- `PATCH /api/v1/categories/{id}/`
- `DELETE /api/v1/categories/{id}/`

## Auth JWT

- `POST /api/v1/auth/token/`
- `POST /api/v1/auth/token/refresh/`
- `GET /api/v1/auth/me/` (requiert un header `Authorization: Bearer <access_token>`)

## Médicaments

- `GET /api/v1/medicaments/`
- `POST /api/v1/medicaments/`
- `GET /api/v1/medicaments/{id}/`
- `PATCH /api/v1/medicaments/{id}/`
- `DELETE /api/v1/medicaments/{id}/` (soft delete)
- `GET /api/v1/medicaments/alertes/`

### Filtres utiles

- `search=<texte>`
- `categorie=<id>`
- `ordonnance_requise=true|false`
- `page=<n>` et `page_size=<n>`

## Ventes

- `GET /api/v1/ventes/`
- `POST /api/v1/ventes/`
- `GET /api/v1/ventes/{id}/`
- `POST /api/v1/ventes/{id}/annuler/`

### Filtres utiles

- `statut=COMPLETEE|ANNULEE`
- `date_vente_debut=YYYY-MM-DD`
- `date_vente_fin=YYYY-MM-DD`

## Exemples de scénarios métier

### Scénario 1 — Gestion d'inventaire

1. Créer une catégorie
2. Créer un médicament avec `stock_actuel <= stock_minimum`
3. Vérifier qu'il est présent dans `GET /medicaments/alertes/`
4. Archiver le médicament via `DELETE /medicaments/{id}/`
5. Vérifier qu'il ne remonte plus dans la liste active

### Scénario 2 — Vente complète

1. Créer une vente avec plusieurs lignes via `POST /ventes/`
2. Vérifier que le `total_ttc` correspond à la somme des sous-totaux
3. Vérifier la déduction de stock de chaque médicament
4. Vérifier l'historique via `GET /ventes/`

### Scénario 3 — Annulation de vente

1. Prendre une vente existante
2. Appeler `POST /ventes/{id}/annuler/`
3. Vérifier le statut `ANNULEE`
4. Vérifier la réintégration du stock

## Structure de réponse d'erreur (normalisée)

```json
{
  "status_code": 400,
  "error": "validation_error",
  "detail": "..."
}
```