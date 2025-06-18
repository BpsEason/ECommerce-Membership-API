from sqlalchemy.orm import Session, joinedload
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..auth import get_password_hash
from datetime import datetime

def get_user(db: Session, user_id: int):
    """根據使用者 ID 獲取使用者，包含地址"""
    return db.query(User).options(joinedload(User.addresses)).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """根據使用者名稱獲取使用者"""
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    """根據電子郵件獲取使用者"""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """創建新使用者"""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        phone_number=user.phone_number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    """更新使用者資訊"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        update_data = user_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def update_user_password(db: Session, user_id: int, hashed_password: str):
    """更新使用者密碼"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.hashed_password = hashed_password
        db.commit()
        db.refresh(db_user)
    return db_user

def update_user_last_login(db: Session, user_id: int):
    """更新使用者上次登入時間"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.last_login_at = datetime.utcnow()
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """刪除使用者"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user