from datetime import timedelta

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from greenletio import async_
from sqlalchemy.orm import Session
from starlette import status

from emprega_vale import schemas, crud
from emprega_vale.api.dependencies import get_db
from emprega_vale.config import settings as stg
from emprega_vale.contrib.auth import verify_password, create_token

router = APIRouter()


@router.post('/register', response_model=schemas.User, status_code=201)
async def create_user(*, user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = await async_(crud.login.create)(db, user_in)

    return user


@router.post('/login', response_model=schemas.Token, status_code=201)
async def login_user(login: schemas.Login, db: Session = Depends(get_db)):
    if user := crud.login.get_by_email(db, login.email):
        if verify_password(login.password, user.password):
            access_token = create_token(user.uid)
            refresh_token = create_token(user.uid, timedelta(minutes=stg.JWT_REFRESH_EXPIRE_MINUTES))
            return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'Bearer'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Wrong Email or Password',
        headers={'WWW-Authenticate': 'Bearer'},
    )


def init_app(app: FastAPI):
    app.include_router(router, prefix='/auth', tags=['Auth'])
