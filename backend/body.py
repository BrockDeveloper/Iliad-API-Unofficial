from pydantic import BaseModel


class AuthRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    token: str