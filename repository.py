from typing import Any, Sequence, Tuple
from sqlalchemy import Result, Select, select
from database import BooksORM, UserORM, new_session
from schemas import SBookAdd, SUserAdd


class BookRepository:
  @classmethod
  async def add_book(cls, data: SBookAdd):
    async with new_session() as session:
      book_dict = data.model_dump()
      book = BooksORM(**book_dict)
      session.add(book)
      await session.flush()
      await session.commit()
      return book.id
    

  @classmethod
  async def find_all(cls):
    async with new_session() as session:
      query: Select[Tuple[BooksORM]] = select(BooksORM)
      result: Result[Tuple[BooksORM]] = await session.execute(query)
      book_models: Sequence[BooksORM] = result.scalars().all()
      return book_models
    

class UserRepository:
  @classmethod
  async def add_user(cls, data: SUserAdd):
    async with new_session() as session:
      user_dict: dict[str, Any] = data.model_dump()
      user = UserORM(**user_dict)
      session.add(user)
      await session.flush()
      await session.commit()
      return user.id
    

  @classmethod
  async def find_all(cls):
    async with new_session() as session:
      query: Select[Tuple[UserORM]] = select(UserORM)
      result: Result[Tuple[UserORM]] = await session.execute(query)
      user_models: Sequence[UserORM] = result.scalars().all()
      return user_models