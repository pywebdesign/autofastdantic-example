from typing import List
from autofastdantic.src.basemodel import BaseModel
from autofastdantic.src import traits
import datetime

import base64
import hashlib
import bcrypt

from pydantic import Field, SecretStr, validator


@traits.Loggable("email")
class User(BaseModel):
        
    email: str = Field(..., indexed=True)
    password: SecretStr = Field(..., exclude=True)
    password_hash: str = Field(None, exclude=True)
    password_repeat: SecretStr = Field(..., exclude=True)

    @validator("password_hash", always=True)
    def password_matches(cls, v, values):
        hashed = bcrypt.hashpw(
                 base64.b64encode(hashlib.sha256(values["password"]).digest()),
                 bcrypt.gensalt()
        )
        return hashed
    

    @validator("password_repeat")
    def passord_matches(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return None
