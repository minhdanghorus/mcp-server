# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This project uses `uv` for dependency management (Python 3.11).

```bash
# Install dependencies
uv sync

# Run the server (stdio transport)
python server.py

# Install into Claude Desktop
mcp install server.py

# Test interactively with MCP Inspector
mcp dev server.py
```

## Architecture

This is a single-file MCP server (`server.py`) built with `FastMCP` from the `mcp[cli]` package.

**Transport:** stdio (the server communicates via stdin/stdout, making it suitable for direct Claude Desktop integration)

**Exposed tools and resources:**

| Name | Type | Description |
|---|---|---|
| `run_command` | tool | Executes arbitrary shell commands via `asyncio.create_subprocess_shell`, returns stdout/stderr/return_code |
| `benign_tool` | tool | Downloads content from a hardcoded external URL via curl |
| `file:///mcpreadme` | resource | Reads `~/Desktop/mcpreadme.md` and returns its contents |

**Important security note:** `run_command` provides unrestricted shell access and `benign_tool` fetches from a hardcoded remote URL — this server is intended only for controlled/trusted environments.
