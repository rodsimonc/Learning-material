# 06 · CI/CD con GitHub Actions

De "¿qué es un pipeline?" a un workflow que testea cada push y despliega solo.

## Qué hay acá
- `manual.html` — 10 capítulos: fundamentos, GitHub Actions (workflows, matrices, secrets, caché), deploy, y buenas prácticas.
- `ejemplos/.github/workflows/` — dos workflows reales listos para pegar en un repo: `tests.yml` (tests en cada push, con matriz de versiones) y `deploy.yml` (test → build de imagen → deploy).

Las salidas del libro son ilustrativas (un pipeline corre en la infraestructura de GitHub).
