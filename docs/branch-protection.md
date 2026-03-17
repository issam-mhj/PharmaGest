# Branch Protection & Review Strategy

## Target branches

- `main`: stable branch, always releasable
- `develop`: optional integration branch for grouped feature work

## Recommended protection rules

Configurer ces règles sur GitHub ou GitLab au niveau du dépôt distant :

### For `main`
- Require pull request before merging
- Require at least 1 approving review
- Dismiss stale approvals when new commits are pushed
- Require conversation resolution before merge
- Restrict direct pushes
- Require linear history if team workflow prefers rebase/squash

### For `develop` (if used)
- Require pull request before merging
- Require at least 1 review for risky or cross-cutting changes
- Restrict direct pushes to maintain traceability

## Review strategy

### Reviewer assignment
- Backend-only PRs: backend reviewer
- Frontend-only PRs: frontend reviewer
- Cross-stack PRs: one reviewer from each side
- Repo/process PRs: tech lead or shared reviewer group

### Merge rules
- Prefer squash merge for small feature branches
- Keep PRs focused on one concern
- Reject PRs with unrelated formatting or mixed responsibilities

## Important note

Les protections de branches ne peuvent pas être activées localement depuis le workspace seul. Ce document décrit la configuration à appliquer sur la plateforme distante du dépôt.
