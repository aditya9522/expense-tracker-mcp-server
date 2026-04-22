from fastmcp.tools import tool
from db import get_connection
from datetime import datetime
from models import ExpenseInput

@tool()
def add_expense(expense: ExpenseInput):
    conn = get_connection()
    cursor = conn.cursor()

    date = expense.date or datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (expense.amount, expense.category, expense.description, date))

    conn.commit()
    conn.close()

    return {"status": "success", "message": "Expense added"}