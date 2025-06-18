from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from .address import Address

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="使用者名稱")
    email: EmailStr = Field(..., description="電子郵件")
    full_name: Optional[str] = Field(None, max_length=100, description="真實姓名")
    phone_number: Optional[str] = Field(None, max_length=20, description="聯絡電話")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="密碼")

class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None

class UserPasswordUpdate(BaseModel):
    old_password: str = Field(..., description="舊密碼")
    new_password: str = Field(..., min_length=6, description="新密碼")

class User(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: Optional[datetime]
    addresses: List[Address] = []

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str