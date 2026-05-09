## Profundus MCP Forge

**Elite Enhanced Profundus Research Agent** — ruthless triangulation, OSS destruction, and production-grade MCP connector.

### Quick Deploy (Railway)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkwizzlesurp10-ctrl%2Fprofundus-mcp-forge)

### Local Development & Debugging (Recommended)

```bash
git clone https://github.com/kwizzlesurp10-ctrl/profundus-mcp-forge.git
cd profundus-mcp-forge
pip install -r requirements.txt

# Run locally (simulates Railway)
python -m servers.python.main

# Or with uvicorn for FastAPI testing
uvicorn servers.python.main:app --reload --port 8000
```

**Debugging Tips**:
- Check logs for `FastMCP initialized successfully` or errors
- Health endpoint: `http://localhost:8000/health`
- Common issues: wrong `mcp` version, missing imports, or constructor kwargs
- To test changes locally before pushing: run the above commands

### CI Security (Active)
- Gitleaks + TruffleHog secret scanning
- CodeQL (Python) + Dependency Review on PRs
- GitHub Advanced Security enabled

### Current Tools
- `profundus_triangulate`
- `oss_repo_audit`

**Version**: 0.1.0 | **Last Updated**: 2026-05-09

**Goal**: Fix future errors in one take via local testing + defensive code + CI smoke tests.