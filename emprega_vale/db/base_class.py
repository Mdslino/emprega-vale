from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from emprega_vale.contrib.utils import to_camel


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True, nullable=False)
    uid = Column(UUID(as_uuid=True), unique=True, index=True, nullable=False, default=uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now, default=None)

    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class PydanticBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = to_camel
