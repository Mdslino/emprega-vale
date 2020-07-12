from datetime import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from emprega_vale.config import settings as stg

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'postgresql://{stg.DB_USER}:{stg.DB_PASS}@{stg.DB_HOST}:{stg.DB_PORT}/{stg.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AlchemyBase = declarative_base()


class AlchemyBaseModel(AlchemyBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True, nullable=True)
    uid = Column(UUID(as_uuid=True), unique=True, index=True, nullable=False, default=uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now, default=None)

    def save(self, session: SessionLocal):
        self.created_at = datetime.now()
        session.add(self)
        session.commit()

    def update(self, session: SessionLocal):
        self.updated_at = datetime.now()
        session.add(self)
        session.commit()

    def delete(self, session: SessionLocal):
        session.delete(self)
        session.commit()
