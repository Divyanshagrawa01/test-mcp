from fastmcp import FastMCP
import json
import asyncio

mcp = FastMCP("Remote MCP Server")


# -------------------------
# TOOLS
# -------------------------

@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
async def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
async def greet(name: str) -> str:
    """Generate a greeting."""
    return f"Hello {name}! Welcome to Remote MCP."

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""

    info = {
        "name": "Remote MCP Server",
        "version": "1.0.0",
        "description": "A remote MCP server with calculator tools",
        "tools": ["add", "multiply", "greet"],
        "author": "Divyansh Agrawal"
    }

    return json.dumps(info, indent=2)



# -------------------------
# RUN SERVER
# -------------------------

if __name__ == "__main2__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
