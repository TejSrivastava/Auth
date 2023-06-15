from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY='d3aeac27ed1407c47c8d69169036e9201be1a3349c290be8abbc1a839b50d5bd'
ALGORITHM='H5256'
ACCESS_TOKEN_EXPIRE_MINUTES=30


app=FastAPI()

fake_db= {
    "tejas": {
        "Username":"Tejas",
        "Full_Name":"Tejas Srivastava",
        "Email":"xyz@gmail.com",
        "Hashed_Password" : "ifj",
        "Disabled": False
        
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str or None = None