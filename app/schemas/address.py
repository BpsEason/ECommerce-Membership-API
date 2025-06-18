from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AddressBase(BaseModel):
    address_line1: str = Field(..., description="地址第一行")
    address_line2: Optional[str] = Field(None, description="地址第二行")
    city: str = Field(..., description="城市")
    state_province: str = Field(..., description="省/州")
    zip_code: str = Field(..., description="郵遞區號")
    country: str = Field(..., description="國家")
    is_default: bool = Field(False, description="是否為預設地址")

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None
    is_default: Optional[bool] = None

class Address(AddressBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True