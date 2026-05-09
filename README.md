## Profundus MCP Forge

**Elite Enhanced Profundus Research Agent** — ruthless triangulation, OSS destruction, and production-grade MCP connector.

### Quick Deploy (Railway)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkwizzlesurp10-ctrl%2Fprofundus-mcp-forge)

### Local Development & Debugging (Strongly Recommended)

```bash
git clone https://github.com/kwizzlesurp10-ctrl/profundus-mcp-forge.git
cd profundus-mcp-forge
pip install -r requirements.txt

# Run the local smoke test (catches 90% of errors before push)
python scripts/test_local.py

# Start the server
python -m servers.python.main

# Or with hot reload
uvicorn servers.python.main:app --reload --port 8000
```

**Pre-commit hooks** (highly recommended):
```bash
pip install pre-commit
pre-commit install
```
This runs the smoke test automatically before every commit.

**Debugging Tips**:
- Run `python scripts/test_local.py` locally first
- Check `/health` for `mcp_initialized` status
- Common issues: wrong `mcp` version or constructor arguments

### CI Security (Active)
- Gitleaks + TruffleHog secret scanning
- CodeQL (Python) + Dependency Review on PRs
- GitHub Advanced Security enabled

### Current Tools
- `profundus_triangulate`
- `oss_repo_audit`

**Version**: 0.1.0 | **Last Updated**: 2026-05-09

**Next Target**: Full local + Railway parity testing workflow (in progress)