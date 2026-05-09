## Profundus MCP Forge

**Elite Enhanced Profundus Research Agent** — ruthless triangulation, OSS destruction, and production-grade MCP connector.

### Quick Deploy (Railway)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkwizzlesurp10-ctrl%2Fprofundus-mcp-forge)

### Local Development (Recommended Workflow)

```bash
# 1. One-time setup
make install

# 2. Before every push (catches 95%+ of errors)
make test

# 3. Run locally
make run

# Or with hot reload
uvicorn servers.python.main:app --reload --port 8000
```

**Makefile targets**:
- `make test` — Full smoke test (health + actual tool invocation + timing)
- `make run` — Start server
- `make pre-commit` — Run all pre-commit hooks
- `make install` — Install everything

**Pre-commit hooks** are active and will run `make test` automatically on commit.

### Current Tools
- `profundus_triangulate` (now tested in smoke test)
- `oss_repo_audit`

**Version**: 0.1.0 | **Last Updated**: 2026-05-09

**Next Target**: Full local + Railway parity testing workflow (Docker + CI matrix) — in progress.