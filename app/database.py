from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 從環境變數獲取資料庫 URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")

# 創建 SQLAlchemy 引擎
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# 創建會話工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基礎模型類
Base = declarative_base()

def get_db():
    """獲取資料庫會話，確保使用後關閉"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()