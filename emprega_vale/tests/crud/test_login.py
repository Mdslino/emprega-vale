from sqlalchemy.orm import Session

from emprega_vale import crud
from emprega_vale.schemas import UserCreate


def test_create_login(db: Session) -> None:
    email = 'random_email@domain.com'
    password = 'admin'

    login_in = UserCreate(email=email, password1=password, password2=password)

    login = crud.login.create(db, login_in)

    assert login.email == email
    assert login.password != password
