from sqlalchemy.orm import Session

from emprega_vale.contrib.auth import get_password_hash
from emprega_vale.crud.base import CRUDBase
from emprega_vale.models import Login
from emprega_vale.schemas.login import LoginCreate, LoginUpdate


class CRUDLogin(CRUDBase[Login, LoginCreate, LoginUpdate]):
    def create(self, db: Session, obj_in: LoginCreate) -> Login:
        db_obj = self.model(email=obj_in.email, password=get_password_hash(obj_in.password1))

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj


login = CRUDLogin(Login)
