from fastmcp import FastMCP
from fastmcp.resources import resource
from fastmcp.prompts import prompt
from fastmcp.tools import tool
from db import init_db, get_connection

# Import tools
from tools.add_expense import add_expense
from tools.get_expenses import get_expenses
from tools.summary import monthly_summary
from tools.delete_expense import delete_expense

# Initialize DB
init_db()

# Create MCP server
mcp = FastMCP("Expense Tracker")

# Register tools
mcp.add_tool(add_expense)
mcp.add_tool(get_expenses)
mcp.add_tool(monthly_summary)
mcp.add_tool(delete_expense)


# Resources

@resource("expense://categories")
def expense_categories():
    return [
        "food",
        "transport",
        "shopping",
        "bills",
        "health",
        "education",
        "entertainment",
        "general"
    ]

@resource("budget://monthly_budget")
def monthly_budget():
    return {
        "food": 5000,
        "transport": 2000,
        "shopping": 3000
    }

@resource("expenses://recent_expenses")
def recent_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT amount, category, date
        FROM expenses
        ORDER BY date DESC
        LIMIT 10
    """)

    data = cursor.fetchall()
    conn.close()

    return data



# MCP Prompts

@prompt()
def categorize_expense():
    return """
    Given a description, assign the best category.

    Example:
    "Swiggy order" → food
    "Uber ride" → transport
    """

# Intelligent Tools

@tool()
def check_budget(month: str):
    summary = monthly_summary(month)
    budget = monthly_budget()

    alerts = {}

    for category, spent in summary.items():
        if category in budget and spent > budget[category]:
            alerts[category] = f"Exceeded by {spent - budget[category]}"

    return alerts



if __name__ == "__main__":
    # mcp.run()   # Local mcp server
    mcp.run(transport="http", host="0.0.0.0", port=8000)            # Remote mcp server for deployment