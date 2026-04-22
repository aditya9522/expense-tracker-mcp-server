from pydantic import BaseModel
from typing import Optional

class ExpenseInput(BaseModel):
    amount: float
    category: Optional[str] = "general"
    description: Optional[str] = ""
    date: Optional[str] = None