from fastmcp.tools import tool
from db import get_connection

@tool()
def delete_expense(expense_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

    return {"status": "deleted"}