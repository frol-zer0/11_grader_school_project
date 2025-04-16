from typing import Annotated, Sequence
from fastapi import APIRouter, Depends
from database import BooksORM, UserORM
from repository import *
from schemas import *


book_router = APIRouter(
  prefix="/books",
  tags=["Книги"]
)


user_router = APIRouter(
  prefix="/users",
  tags=["Пользователи"]
)


@book_router.post("")
async def add_book(
  book: Annotated[SBookAdd, Depends()]
):
  book_id: int = await BookRepository.add_book(book)
  return {"ok" : True, "book_id": book_id}



@book_router.get("")
async def get_books():
  books: Sequence[BooksORM] = await BookRepository.find_all()
  return {"books": books}


@user_router.post("")
async def add_user(
  user: Annotated[SUserAdd, Depends()]
):
  uid: int = await UserRepository.add_user(user)
  return {"ok" : True, "uid": uid}


@user_router.get("")
async def get_users():
  users: Sequence[UserORM] = await UserRepository.find_all()
  return {"users": users}