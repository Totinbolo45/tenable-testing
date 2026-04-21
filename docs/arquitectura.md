# Arquitectura del proyecto

## Flujo general

1. **GitHub Actions** lanza el workflow (`tenable-scan.yml`).
2. **`src/scanner/`** inicia un escaneo en Tenable y recoge los resultados.
3. **`src/ai/`** envía los resultados a la IA para que los interprete.
4. **`src/report/`** genera un informe final en formato humano.
5. El informe se publica (commit automático, PR o artifact).

## Diagrama

```
GitHub Actions
      │
      ▼
  scanner/  ──► Tenable API
      │
      ▼
     ai/  ──► modelo IA
      │
      ▼
  report/  ──► informe final (Markdown)
```
