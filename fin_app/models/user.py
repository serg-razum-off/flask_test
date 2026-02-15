from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    email: str
    date_created: datetime
    date_updated: datetime
