from datetime import timedelta, datetime
from typing import Union
from uuid import UUID

from authlib.jose import jwt, JWTClaims
from authlib.jose.errors import BadSignatureError, InvalidClaimError
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext

from emprega_vale.config import settings as stg

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(subject: Union[str, UUID], expires_delta: timedelta = None) -> str:
    header = {'alg': stg.JWT_ALG}
    payload = {'iss': stg.NAME, 'sub': str(subject)}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=stg.JWT_ACCESS_EXPIRE_MINUTES)

    payload.update({'exp': expire})

    encoded_jwt = jwt.encode(header, payload, stg.SECRET)

    return encoded_jwt.decode()


def verify_token(token: str) -> JWTClaims:
    try:
        claims = jwt.decode(token, stg.SECRET)
        claims.validate()
        return claims
    except (BadSignatureError, InvalidClaimError):
        raise HTTPException(401, {'description': 'Invalid Token'})
