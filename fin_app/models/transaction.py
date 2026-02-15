from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Category(str, Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    HOUSING = "Housing"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


class Transaction(BaseModel):
    id: int
    amount: float
    description: str
    category: Category
    date_created: datetime
    date_updated: datetime
