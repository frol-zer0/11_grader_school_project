from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SBookAdd(BaseModel):
  name: str
  author: str
  genres: str
  description: Optional[str] = None


class Books(SBookAdd):
  id: int
  name: str
  author: str
  genres: str
  description: Optional[str] = None

class SUserAdd(BaseModel):
  username: str
  password: str
  finished_books: int
  description: Optional[str] = None

class Users(SUserAdd):
  id: int
  registration_date: datetime
  username: str
  password: str
  finished_books: int
  description: Optional[str] = None
  
