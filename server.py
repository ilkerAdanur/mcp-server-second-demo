from mcp.server.fastmcp import FastMCP
from app import getliveTemp

# Initialize MCP server
mcp = FastMCP("weather-forecast-mcp")

@mcp.tool()
async def get_live_temp(latitude: float, longitude: float) -> Dict[str, Any]:
    """Ask for temp value matching specific keywords."""
    return getliveTemp(latitude, longitude)

if __name__ == "__main__":
    mcp.run(transport="stdio")