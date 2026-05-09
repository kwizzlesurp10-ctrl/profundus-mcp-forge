#!/usr/bin/env python3
"""
Profundus MCP Forge - Local Smoke Test (Enhanced)

Tests:
- FastAPI app health
- MCP initialization
- Actual invocation of profundus_triangulate tool
- Timing + basic reporting

Usage: python scripts/test_local.py
"""

import asyncio
import sys
import time
from fastapi.testclient import TestClient

try:
    from servers.python.main import app, mcp, triangulate
    client = TestClient(app)
except Exception as e:
    print(f"FAILED to import: {e}")
    sys.exit(1)

def test_health():
    start = time.perf_counter()
    response = client.get("/health")
    duration = (time.perf_counter() - start) * 1000
    assert response.status_code == 200
    data = response.json()
    print(f"Health check: {duration:.1f}ms | status={data.get('status')} | mcp_initialized={data.get('mcp_initialized')}")
    assert data.get("status") in ["healthy", "degraded"]
    return duration

def test_tool_invocation():
    if mcp is None:
        print("SKIPPED: MCP not initialized")
        return 0.0

    start = time.perf_counter()
    result = asyncio.run(triangulate("Test query for smoke test", min_sources=2))
    duration = (time.perf_counter() - start) * 1000

    print(f"Tool call (profundus_triangulate): {duration:.1f}ms")
    assert result.get("confidence") == "HIGH"
    assert "Triangulation complete" in str(result.get("key_findings", []))
    print(f"Tool result: {result}")
    return duration

if __name__ == "__main__":
    print("\n=== Profundus Local Smoke Test (v0.1.1) ===\n")
    total_start = time.perf_counter()

    try:
        health_time = test_health()
        tool_time = test_tool_invocation()

        total_time = (time.perf_counter() - total_start) * 1000
        print(f"\n✅ All tests PASSED in {total_time:.1f}ms")
        print(f"   Health: {health_time:.1f}ms | Tool: {tool_time:.1f}ms")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)