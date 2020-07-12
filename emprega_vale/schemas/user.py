from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import constr, EmailStr, validator

from emprega_vale.db.base_class import PydanticBaseModel


class Group(PydanticBaseModel):
    uid: UUID
    name: constr(max_length=50)

    class Config:
        orm_mode = True


class UserBase(PydanticBaseModel):
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    email: EmailStr
    password1: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    uid: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    email: EmailStr
    group: Group

    class Config:
        orm_mode = True


class User(UserInDBBase):
    ...


class UserInDB(UserInDBBase):
    ...
