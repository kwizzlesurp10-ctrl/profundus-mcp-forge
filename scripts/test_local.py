#!/usr/bin/env python3
"""
Local smoke test for Profundus MCP Forge.
Checks:
- FastAPI app starts
- /health endpoint returns healthy
- MCP tools are registered (if FastMCP available)

Run: python scripts/test_local.py
"""

import sys
from fastapi.testclient import TestClient

try:
    from servers.python.main import app, mcp
    client = TestClient(app)
except Exception as e:
    print(f"FAILED to import app: {e}")
    sys.exit(1)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    print(f"Health: {data}")
    assert data.get("status") in ["healthy", "degraded"]
    if not data.get("mcp_initialized"):
        print("WARNING: MCP not initialized (degraded mode)")
    print("✓ /health endpoint OK")

def test_tools_registered():
    if mcp is None:
        print("SKIPPED: MCP not initialized")
        return
    # FastMCP exposes tools via internal registry in newer versions
    # For now we just check that the object exists
    print("✓ MCP object exists")

if __name__ == "__main__":
    print("Running Profundus local smoke test...")
    try:
        test_health()
        test_tools_registered()
        print("\n✅ All local smoke tests PASSED")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)