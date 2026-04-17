from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecret"   # 🔥 change en prod
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password: str):
    return pwd_context.hash(password)



def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

from app.core.config import settings

security = HTTPBearer()


def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(
            token.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")