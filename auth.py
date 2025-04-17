from fastapi import HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config = config)


class UserLoginSchema(BaseModel):
  username: str
  password: str



