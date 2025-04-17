from typing import Annotated, Sequence
from fastapi import APIRouter, Depends, HTTPException, Response, security
from database import BooksORM, UserORM
from repository import *
from schemas import *
from auth import *

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


@user_router.post("")
async def add_user(
  user: Annotated[SUserAdd, Depends()]
):
  uid: int = await UserRepository.add_user(user)
  return {"ok" : True, "uid": uid}


@user_router.post("/login")
def login(creds: UserLoginSchema, response: Response):
  if creds.username == "adam" and creds.password == "123":
    token = security.create_access_token(uid="12345")
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
    return {"access_token": token}
  raise HTTPException(status_code=401, detail="Incorrect username or password")



@user_router.get("")
async def get_users():
  users: Sequence[UserORM] = await UserRepository.find_all()
  return {"users": users}


@book_router.get("")
async def get_books():
  books: Sequence[BooksORM] = await BookRepository.find_all()
  return {"books": books}


@user_router.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
  return {"data": "TOP SECRET"}
