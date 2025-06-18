from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import users, auth
from database import engine
from models.user import User
from models.address import Address

app = FastAPI(
    title="電子商務會員系統",
    description="基於 FastAPI 的可擴展電子商務會員系統",
    version="1.0.0"
)

# 創建資料庫表
User.metadata.create_all(bind=engine)
Address.metadata.create_all(bind=engine)

# CORS 中介軟體，方便前端整合
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生產環境應限制特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含路由
app.include_router(auth.router, prefix="/auth", tags=["認證"])
app.include_router(users.router, prefix="/users", tags=["使用者"])

@app.get("/")
async def root():
    """根端點，用於健康檢查"""
    return {"message": "電子商務會員系統 API"}