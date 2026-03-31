from pydantic import BaseModel
from datetime import datetime


class News(BaseModel):
    id: int
    title: str
    content: str
    author: str
    category: str
    created_at: datetime
    is_published: bool