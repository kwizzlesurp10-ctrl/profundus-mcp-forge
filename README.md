## Profundus MCP Forge

**Elite Enhanced Profundus Research Agent** — ruthless triangulation, OSS destruction, and production-grade MCP connector.

### Quick Deploy (Railway)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fkwizzlesurp10-ctrl%2Fprofundus-mcp-forge)

**One-click deploy**:
1. Click the button above
2. Connect your GitHub account
3. Railway will auto-detect Python + run `python -m servers.python.main`
4. Health endpoint: `https://your-app.up.railway.app/health`

**Environment Variables** (optional):
- `PORT` (auto-set by Railway)

### Local Development
```bash
git clone https://github.com/kwizzlesurp10-ctrl/profundus-mcp-forge.git
cd profundus-mcp-forge
pip install -r requirements.txt
python -m servers.python.main
```

### CI Security (Active)
- Gitleaks + TruffleHog secret scanning on every push/PR
- Weekly full-history scan
- CodeQL (Python) + Dependency Review on PRs
- GitHub Advanced Security (public repo default)

### MCP Tools Exposed
- `profundus_triangulate` — multi-source ruthless research
- `oss_repo_audit` — forensic repo analysis

**Version**: 0.1.0 | **Last Updated**: 2026-05-09

**Next Targets**: Real tool integration (web_search, browse_page), pre-commit hooks, self-evolution.