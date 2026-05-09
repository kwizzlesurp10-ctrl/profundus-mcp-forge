## Contributing to Profundus MCP Forge

### Development Workflow (Local = Railway Parity)

We follow a strict "test locally first" philosophy to minimize Railway redeploys.

#### 1. One-time Setup
```bash
make install          # Installs dependencies + pre-commit
```

#### 2. Daily Development Loop
```bash
make test             # Run full smoke test (health + real tool call + timing)
# Make your changes
make test             # Verify everything still works
make run              # Test locally if needed
```

#### 3. Before Every Push
```bash
git add .
git commit -m "feat: ..."   # Pre-commit hook runs make test automatically
git push
```

#### 4. CI & Railway
- Every PR runs the same `make test` (full parity)
- Railway uses the same `Dockerfile` + start command
- All changes must pass local + CI tests

### Code Style
- Keep defensive error handling around third-party SDKs (FastMCP, etc.)
- Add timing/logging to new features when possible
- Update smoke test when adding new tools

### Questions?
Open an issue or reach out to the maintainers.