from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class News(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: str
    category: str
    created_at: datetime
    is_published: bool


class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    is_published: Optional[bool] = None
