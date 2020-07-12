from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from emprega_vale.contrib.auth import get_password_hash
from emprega_vale.crud.base import CRUDBase
from emprega_vale.models import User
from emprega_vale.schemas.user import UserCreate, UserUpdate


class CRUDLogin(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, obj_in: UserCreate) -> User:
        try:
            db_obj = self.model(email=obj_in.email, password=get_password_hash(obj_in.password1), group_id=1)

            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

            return db_obj
        except IntegrityError as e:
            raise HTTPException(409, 'A error occur on user creation')

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(self.model).filter_by(email=email).first()


login = CRUDLogin(User)
