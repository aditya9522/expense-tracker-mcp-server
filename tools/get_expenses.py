from fastmcp.tools import tool
from db import get_connection

@tool()
def get_expenses(category: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("SELECT * FROM expenses WHERE category=?", (category,))
    else:
        cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "amount": r[1],
            "category": r[2],
            "description": r[3],
            "date": r[4],
        }
        for r in rows
    ]