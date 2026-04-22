from fastmcp.tools import tool
from db import get_connection

@tool()
def monthly_summary(month: str):
    """
    month format: YYYY-MM
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        WHERE date LIKE ?
        GROUP BY category
    """, (f"{month}%",))

    data = cursor.fetchall()
    conn.close()

    return {category: total for category, total in data}