from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)  # 真實姓名
    phone_number = Column(String, unique=True, index=True, nullable=True)  # 聯絡電話
    is_active = Column(Boolean, default=True)  # 帳戶是否啟用
    is_verified = Column(Boolean, default=False)  # 電子郵件是否驗證
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now())
    last_login_at = Column(DateTime, nullable=True)  # 上次登入時間

    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")  # 關聯送貨地址

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"