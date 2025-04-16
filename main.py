from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from router import book_router, user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan,
              tags=["Книги"])
app.include_router(book_router)
app.include_router(user_router)
