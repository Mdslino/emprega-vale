from pydantic import EmailStr

from emprega_vale.db.base_class import PydanticBaseModel


class Login(PydanticBaseModel):
    email: EmailStr
    password: str


class Token(PydanticBaseModel):
    access_token: str
    refresh_token: str
