from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.user import User, UserUpdate, UserPasswordUpdate
from ..schemas.address import Address, AddressCreate, AddressUpdate
from ..crud.user import update_user, update_user_password, delete_user
from ..crud.address import get_user_addresses, get_address, create_address, update_address, delete_address
from ..auth import get_current_user, verify_password, get_password_hash
from ..models.user import User as DBUser # 導入 SQLAlchemy User 模型

router = APIRouter()

async def get_current_active_user(current_user: DBUser = Depends(get_current_user)):
    """獲取當前活躍使用者"""
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="使用者帳戶未啟用")
    return current_user

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """獲取當前登入使用者的資訊，包含地址"""
    # current_user 已經是完整的 DBUser 對象，Pydantic 會自動轉換
    return current_user

@router.put("/me", response_model=User)
async def update_users_me(user_update: UserUpdate, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """更新當前登入使用者的資訊（非密碼）"""
    updated_user = update_user(db, current_user.id, user_update)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="使用者未找到")
    return updated_user

@router.put("/me/password", response_model=User)
async def update_my_password(password_update: UserPasswordUpdate, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """更新當前登入使用者的密碼"""
    if not verify_password(password_update.old_password, current_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="舊密碼不正確")
    new_hashed_password = get_password_hash(password_update.new_password)
    updated_user = update_user_password(db, current_user.id, new_hashed_password)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="使用者未找到")
    return updated_user

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_users_me(current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """刪除當前登入使用者的帳戶"""
    deleted = delete_user(db, current_user.id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="使用者未找到")
    return {"message": "帳戶已成功刪除"}

@router.get("/me/addresses", response_model=List[Address])
async def read_my_addresses(current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """獲取當前登入使用者的所有送貨地址"""
    addresses = get_user_addresses(db, current_user.id)
    return addresses

@router.post("/me/addresses", response_model=Address, status_code=status.HTTP_201_CREATED)
async def create_my_address(address: AddressCreate, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """為當前登入使用者新增一個送貨地址"""
    return create_address(db, address, current_user.id)

@router.get("/me/addresses/{address_id}", response_model=Address)
async def read_my_address(address_id: int, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """獲取當前登入使用者指定 ID 的送貨地址"""
    address = get_address(db, address_id)
    if not address or address.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="地址未找到或不屬於此使用者")
    return address

@router.put("/me/addresses/{address_id}", response_model=Address)
async def update_my_address(address_id: int, address_update: AddressUpdate, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """更新當前登入使用者指定 ID 的送貨地址"""
    updated_address = update_address(db, address_id, address_update, current_user.id)
    if not updated_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="地址未找到或不屬於此使用者")
    return updated_address

@router.delete("/me/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_my_address(address_id: int, current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    """刪除當前登入使用者指定 ID 的送貨地址"""
    deleted = delete_address(db, address_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="地址未找到或不屬於此使用者")
    return {"message": "地址已成功刪除"}