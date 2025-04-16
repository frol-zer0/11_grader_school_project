import datetime
import token
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from typing import Optional


book_engine: AsyncEngine = create_async_engine(
  "sqlite+aiosqlite:///tables//books.db"
)


user_engine: AsyncEngine = create_async_engine(
  "sqlite+aiosqlite:///tables//users.db"
)


new_session = async_sessionmaker(book_engine, expire_on_commit = False)

class Model(DeclarativeBase):
  pass


class BooksORM(Model):
  __tablename__ = "books"

  id: Mapped[int] = mapped_column(primary_key = True)
  name: Mapped[str]
  author: Mapped[str]
  genres: Mapped[str]
  description: Mapped[Optional[str]]


class UserORM(Model):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key = True)
  username: Mapped[str]
  password: Mapped[str]
  finished_books: Mapped[int]
  description: Mapped[Optional[str]]


async def create_tables():
  async with book_engine.begin() as conn:
    await conn.run_sync(Model.metadata.create_all)
  
  async with user_engine.begin() as conn:
    await conn.run_sync(Model.metadata.create_all)
   


async def drop_tables():
  async with book_engine.begin() as conn:
    await conn.run_sync(Model.metadata.drop_all)