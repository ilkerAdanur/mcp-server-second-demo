from mcp.server.fastmcp import FastMCP
from app import convert_currency

mcp = FastMCP("currency-converter-mcp")

@mcp.tool()
async def convert_currency_tool(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Convert currency using exchangerate.host API.
    """
    result = convert_currency(amount, from_currency, to_currency)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
