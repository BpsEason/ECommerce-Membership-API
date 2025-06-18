# 🛒 電子商務會員系統 API

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.103.0-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy Version](https://img.shields.io/badge/SQLAlchemy-2.0.20-orange.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docker Hub](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

這是一個基於 **FastAPI** 框架構建的電子商務會員系統後端 API。此專案旨在提供一個高可讀性、可維護且易於擴展的基礎，適用於現代電子商務平台。它具備完整的會員生命週期管理、安全的身份驗證機制以及彈性的送貨地址管理功能。

## ✨ 專案特色

- **使用者管理**：
  - 新會員註冊
  - 會員登入（JWT 認證）
  - 獲取/更新個人資料（姓名、電話）
  - 安全地更新密碼（需驗證舊密碼）
  - 帳戶刪除
  - 模擬的電子郵件驗證與密碼重設流程（需擴展實際發送郵件服務）
- **送貨地址管理**：
  - 為使用者新增多個送貨地址
  - 查詢所有或單一送貨地址詳情
  - 更新現有送貨地址資訊
  - 刪除送貨地址
  - 自動管理預設地址，確保單一預設地址邏輯
- **安全認證**：
  - 基於 JWT (JSON Web Token) 的身份認證機制
  - 密碼使用強大的 `bcrypt` 雜湊演算法儲存
  - 通過 OAuth2 `Password Flow` 實現標準登入流程
- **模組化設計**：
  - 清晰的專案結構，依功能劃分為 `models`、`schemas`、`crud`、`routers` 等模組，易於擴展和維護
  - 利用 FastAPI 的依賴注入 (Dependency Injection) 管理資料庫會話和認證狀態
- **自動化 API 文件**：
  - 內建 Swagger UI 和 ReDoc，提供互動式 API 文件，方便測試與協作
- **測試與部署**：
  - 包含單元測試，確保核心功能正確性
  - 支援 Docker 容器化部署，提供 `Dockerfile` 和 `docker-compose.yml`，簡化部署流程

## 🛠️ 技術棧

- **後端框架**：[FastAPI](https://fastapi.tiangolo.com/) (0.103.0) - 高性能、易於使用的現代 Python Web 框架
- **資料庫 ORM**：[SQLAlchemy](https://www.sqlalchemy.org/) (2.0.20) - Python 的 ORM 工具，支援多種資料庫（預設 SQLite，易於切換至 PostgreSQL/MySQL）
- **資料驗證**：[Pydantic](https://pydantic-docs.helpmanual.io/) (2.4.2) - 基於 Python 型別提示的資料驗證和設定管理
- **認證與安全**：
  - [python-jose](https://python-jose.readthedocs.io/en/latest/) (3.3.0) - 處理 JWT (JSON Web Token)
  - [passlib](https://passlib.readthedocs.io/en/stable/) (1.7.4) - 提供安全的密碼雜湊功能（bcrypt）
- **環境管理**：[python-dotenv](https://github.com/theskumar/python-dotenv) (1.0.0) - 從 `.env` 檔案載入環境變數
- **WSGI/ASGI 伺服器**：[Uvicorn](https://www.uvicorn.org/) (0.23.2) - FastAPI 推薦的 ASGI 伺服器
- **測試框架**：[pytest](https://docs.pytest.org/en/stable/) (7.4.0)
- **HTTP 客戶端**：[httpx](https://www.python-httpx.org/) (0.24.1) - 用於非同步測試和 API 請求
- **容器化**：[Docker](https://www.docker.com/)、[Docker Compose](https://docs.docker.com/compose/)

## 📂 專案結構

```plaintext
.
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI 主應用程式，負責路由整合與資料庫初始化
│   ├── database.py         # 資料庫連接配置與會話管理 (SQLAlchemy)
│   ├── auth.py             # 認證邏輯：密碼雜湊、JWT 生成與驗證
│   ├── models/             # SQLAlchemy 資料庫模型定義 (表的結構)
│   │   ├── __init__.py
│   │   ├── user.py         # 使用者模型
│   │   └── address.py      # 送貨地址模型
│   ├── schemas/            # Pydantic 資料驗證模型 (API 輸入/輸出資料格式)
│   │   ├── __init__.py
│   │   ├── user.py         # 使用者相關的 Pydantic Schema
│   │   └── address.py      # 送貨地址相關的 Pydantic Schema
│   ├── crud/               # CRUD (Create, Read, Update, Delete) 操作邏輯
│   │   ├── __init__.py
│   │   ├── user.py         # 使用者資料庫操作
│   │   └── address.py      # 送貨地址資料庫操作
│   └── routers/            # API 路由定義 (端點邏輯)
│       ├── __init__.py
│       ├── auth.py         # 認證相關 API 端點 (註冊、登入、密碼重設)
│       └── users.py        # 使用者個人資訊與地址管理 API 端點
├── .env                    # 環境變數配置文件 (敏感資訊，不應提交到 Git)
├── requirements.txt        # Python 依賴列表
├── tests/                  # 測試檔案目錄
│   ├── __init__.py
│   └── test_users.py       # 使用者相關功能的測試用例
├── Dockerfile              # Docker 映像構建文件
├── docker-compose.yml      # Docker Compose 配置文件，用於多服務部署 (如應用程式和資料庫)
└── README.md               # 專案說明文件
```

## 🚀 快速開始

以下是如何啟動並運行此專案的步驟。

### 步驟 1: 克隆儲存庫

首先，將專案克隆到你的本地機器：

```bash
git clone https://github.com/BpsEason/ECommerce-Membership-API.git
cd ECommerce-Membership-API
```

### 步驟 2: 環境準備

#### 方式一：本地運行（推薦初學者）

1. **創建並啟動虛擬環境**：

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   .\venv\Scripts\activate
   ```

2. **安裝依賴**：

   ```bash
   pip install -r requirements.txt
   ```

3. **創建 `.env` 檔案**：
   在專案根目錄創建一個名為 `.env` 的文件，並添加以下內容：

   ```plaintext
   DATABASE_URL=sqlite:///./ecommerce.db
   SECRET_KEY=your-very-secure-and-random-secret-key
   ```

   **重要**：請替換 `SECRET_KEY` 為一個隨機且安全的字串。你可以使用以下命令生成：

   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

4. **運行應用程式**：

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   應用程式將在 `http://localhost:8000` 啟動。`--reload` 參數會在程式碼變更時自動重啟伺服器，方便開發。

#### 方式二：使用 Docker Compose（推薦）

確保你已經安裝了 Docker 和 Docker Compose。

1. **創建 `.env` 檔案**：
   同上，在專案根目錄創建 `.env` 文件。`docker-compose.yml` 將會引用此文件中的 `SECRET_KEY`。

   ```plaintext
   DATABASE_URL=sqlite:///./ecommerce.db
   SECRET_KEY=your-very-secure-and-random-secret-key
   ```

2. **構建並啟動服務**：

   ```bash
   docker-compose up --build -d
   ```

   - `--build`：強制重新構建 Docker 映像（初次運行或 `Dockerfile`/`requirements.txt` 變更後使用）。
   - `-d`：在後台模式運行容器。

3. **檢查服務狀態**：

   ```bash
   docker-compose ps
   ```

4. **停止服務**：

   ```bash
   docker-compose down
   ```

## 📄 API 文件

一旦應用程式運行，你可以在瀏覽器中訪問以下 URL 來查看互動式 API 文件：

- **Swagger UI**：`http://localhost:8000/docs`
- **ReDoc**：`http://localhost:8000/redoc`

## 💡 API 端點範例

以下是一些常見的 API 操作範例（使用 `curl`）。請替換 `YOUR_ACCESS_TOKEN` 和其他佔位符。

### 1. 會員註冊

```bash
curl -X POST "http://localhost:8000/auth/register" \
-H "Content-Type: application/json" \
-d '{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "strongpassword123",
  "full_name": "New User",
  "phone_number": "0912345678"
}'
```

### 2. 會員登入（獲取 JWT）

```bash
curl -X POST "http://localhost:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=newuser&password=strongpassword123"
```

響應會包含 `access_token`，請儲存此 token 以用於後續的認證請求。

### 3. 獲取當前使用者資訊（需要認證）

```bash
curl -X GET "http://localhost:8000/users/me" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 4. 更新當前使用者資訊（需要認證）

```bash
curl -X PUT "http://localhost:8000/users/me" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "full_name": "Updated Name",
  "phone_number": "0987654321"
}'
```

### 5. 為當前使用者新增送貨地址（需要認證）

```bash
curl -X POST "http://localhost:8000/users/me/addresses" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "address_line1": "台北市信義區市府路1號",
  "address_line2": "台北101",
  "city": "台北市",
  "state_province": "台灣",
  "zip_code": "110",
  "country": "台灣",
  "is_default": true
}'
```

## 🧪 測試

運行單元測試以驗證功能：

```bash
pytest
```

測試檔案位於 `tests/` 目錄，目前包含使用者註冊的測試用例。未來可擴展更多測試，例如登入、更新資訊、地址管理等。

## 🚀 部署

### 本地部署

推薦使用 `uvicorn` 直接運行：

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 生產環境建議

在生產環境中部署時，請考慮以下最佳實踐：

- **資料庫**：強烈建議使用 **PostgreSQL** 或 **MySQL** 替代 SQLite，以提升性能、可靠性、併發處理能力和資料持久性。更新 `DATABASE_URL` 環境變數即可。
- **密鑰安全**：確保 `SECRET_KEY` 是一個強大且安全的隨機字串。你可以使用以下命令生成：
  ```bash
  python -c "import secrets; print