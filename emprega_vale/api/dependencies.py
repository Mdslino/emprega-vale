from authlib.jose import jwt, JWTClaims
from authlib.jose.errors import DecodeError, InvalidClaimError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from starlette import status

from emprega_vale.config import settings
from emprega_vale.crud import crud_user
from emprega_vale.db.session import SessionLocal

oauth2_scheme = HTTPBearer()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except:  # NOQA
        db.rollback()
    finally:
        db.close()


def user_authenticated(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> JWTClaims:
    try:
        payload = jwt.decode(token.credentials, settings.SECRET)
        payload.validate()
        return payload
    except (DecodeError, InvalidClaimError):
        raise credentials_exception


def get_current_user(payload: JWTClaims = Depends(user_authenticated), db: Session = Depends(get_db)):
    try:
        if user_uid := payload.get('sub'):
            if user := crud_user.login.get_by_uid(db, user_uid):
                return user
            raise credentials_exception
        raise credentials_exception
    except DecodeError:
        raise credentials_exception
