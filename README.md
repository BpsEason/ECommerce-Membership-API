
```markdown
# 🛒 電子商務會員系統 API

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.103.0-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy Version](https://img.shields.io/badge/SQLAlchemy-2.0.20-orange.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docker Hub](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

這是一個基於 **FastAPI** 框架構建的電子商務會員系統後端 API。此專案旨在提供一個高可讀性、可維護且易於擴展的基礎，適用於現代電子商務平台。它具備完整的會員生命週期管理、安全的身份驗證機制以及彈性的送貨地址管理功能。

## ✨ 專案特色

* **使用者管理**：
    * 新會員註冊
    * 會員登入（JWT 認證）
    * 獲取/更新個人資料（姓名、電話）
    * 安全地更新密碼（需驗證舊密碼）
    * 帳戶刪除
    * 模擬的電子郵件驗證與密碼重設流程 (需擴展實際發送郵件服務)
* **送貨地址管理**：
    * 為使用者新增多個送貨地址
    * 查詢所有或單一送貨地址詳情
    * 更新現有送貨地址資訊
    * 刪除送貨地址
    * 自動管理預設地址，確保單一預設地址邏輯
* **安全認證**：
    * 基於 JWT (JSON Web Token) 的身份認證機制
    * 密碼使用強大的 `bcrypt` 雜湊演算法儲存
    * 通過 OAuth2 `Password Flow` 實現標準登入流程
* **模組化設計**：
    * 清晰的專案結構，依功能劃分為 `models`, `schemas`, `crud`, `routers` 等模組，易於擴展和維護
    * 利用 FastAPI 的依賴注入 (Dependency Injection) 管理資料庫會話和認證狀態
* **自動化 API 文件**：
    * 內建 Swagger UI 和 ReDoc，提供互動式 API 文件，方便測試與協作
* **測試與部署**：
    * 包含單元測試，確保核心功能正確性
    * 支援 Docker 容器化部署，提供 `Dockerfile` 和 `docker-compose.yaml`，簡化部署流程

## 🛠️ 技術棧

* **後端框架**：[FastAPI](https://fastapi.tiangolo.com/) (0.103.0) - 高性能、易於使用的現代 Python Web 框架
* **資料庫 ORM**：[SQLAlchemy](https://www.sqlalchemy.org/) (2.0.20) - Python 的 ORM 工具，支援多種資料庫 (預設 SQLite，易於切換至 PostgreSQL/MySQL)
* **資料驗證**：[Pydantic](https://pydantic-docs.helpmanual.io/) (2.4.2) - 基於 Python 型別提示的資料驗證和設定管理
* **認證與安全**：
    * [python-jose](https://python-jose.readthedocs.io/en/latest/) (3.3.0) - 處理 JWT (JSON Web Token)
    * [passlib](https://passlib.readthedocs.io/en/stable/) (1.7.4) - 提供安全的密碼雜湊功能 (bcrypt)
* **環境管理**：[python-dotenv](https://github.com/theskumar/python-dotenv) (1.0.0) - 從 `.env` 檔案載入環境變數
* **WSGI/ASGI 伺服器**：[Uvicorn](https://www.uvicorn.org/) (0.23.2) - FastAPI 推薦的 ASGI 伺服器
* **測試框架**：[pytest](https://docs.pytest.org/en/stable/) (7.4.0)
* **HTTP 客戶端**：[httpx](https://www.python-httpx.org/) (0.24.1) - 用於非同步測試和 API 請求
* **容器化**：[Docker](https://www.docker.com/)、[Docker Compose](https://docs.docker.com/compose/)

## 📂 專案結構

```

.
├── app/
│   ├── **init**.py
│   ├── main.py             \# FastAPI 主應用程式，負責路由整合與資料庫初始化
│   ├── database.py         \# 資料庫連接配置與會話管理 (SQLAlchemy)
│   ├── auth.py             \# 認證邏輯：密碼雜湊、JWT 生成與驗證
│   ├── models/             \# SQLAlchemy 資料庫模型定義 (表的結構)
│   │   ├── **init**.py
│   │   ├── user.py         \# 使用者模型
│   │   └── address.py      \# 送貨地址模型
│   ├── schemas/            \# Pydantic 資料驗證模型 (API 輸入/輸出資料格式)
│   │   ├── **init**.py
│   │   ├── user.py         \# 使用者相關的 Pydantic Schema
│   │   └── address.py      \# 送貨地址相關的 Pydantic Schema
│   ├── crud/               \# CRUD (Create, Read, Update, Delete) 操作邏輯
│   │   ├── **init**.py
│   │   ├── user.py         \# 使用者資料庫操作
│   │   └── address.py      \# 送貨地址資料庫操作
│   └── routers/            \# API 路由定義 (端點邏輯)
│       ├── **init**.py
│       ├── auth.py         \# 認證相關 API 端點 (註冊、登入、密碼重設)
│       └── users.py        \# 使用者個人資訊與地址管理 API 端點
├── .env                    \# 環境變數配置文件 (敏感資訊，不應提交到 Git)
├── requirements.txt        \# Python 依賴列表
├── tests/                  \# 測試檔案目錄
│   ├── **init**.py
│   └── test\_users.py       \# 使用者相關功能的測試用例
├── Dockerfile              \# Docker 映像構建文件
├── docker-compose.yaml     \# Docker Compose 配置文件，用於多服務部署 (如應用程式和資料庫)
└── README.md               \# 專案說明文件

````

## 🚀 快速開始

以下是如何啟動並運行此專案的步驟。

### 步驟 1: 克隆儲存庫

首先，將專案克隆到你的本地機器：

```bash
git clone [https://github.com/BpsEason/ECommerce-Membership-API.git](https://github.com/BpsEason/ECommerce-Membership-API.git)
cd ECommerce-Membership-API
````

### 步驟 2: 環境準備

#### 方式一：本地運行 (推薦初學者)

1.  **創建並啟動虛擬環境**：

    ```bash
    python -m venv venv
    # macOS/Linux
    source venv/bin/activate
    # Windows
    .\venv\Scripts\activate
    ```

2.  **安裝依賴**：

    ```bash
    pip install -r requirements.txt
    ```

3.  **創建 `.env` 檔案**：
    在專案根目錄創建一個名為 `.env` 的文件，並添加以下內容：

    ```dotenv
    DATABASE_URL="sqlite:///./ecommerce.db"
    SECRET_KEY="your-very-secure-and-random-secret-key" # **重要：請替換為一個真正隨機且安全的字串！**
    ```

    你可以使用 `python -c "import secrets; print(secrets.token_hex(32))"` 生成一個強大的 `SECRET_KEY`。

4.  **運行應用程式**：

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

    應用程式將會在 `http://localhost:8000` 啟動。`--reload` 參數會在程式碼變更時自動重啟伺服器，方便開發。

#### 方式二：使用 Docker Compose (推薦)

確保你已經安裝了 Docker 和 Docker Compose。

1.  **創建 `.env` 檔案**：
    同上，在專案根目錄創建 `.env` 文件。`docker-compose.yaml` 將會引用此文件中的 `SECRET_KEY`。

    ```dotenv
    DATABASE_URL="sqlite:///./ecommerce.db" # 也可以在這裡定義，或者直接在 docker-compose.yaml 中定義
    SECRET_KEY="your-very-secure-and-random-secret-key" # **重要：請替換為一個真正隨機且安全的字串！**
    ```

2.  **構建並啟動服務**：

    ```bash
    docker-compose up --build -d
    ```

      * `--build`：強制重新構建 Docker 映像 (初次運行或 `Dockerfile`/`requirements.txt` 變更後使用)。
      * `-d`：在後台模式運行容器。

3.  **檢查服務狀態**：

    ```bash
    docker-compose ps
    ```

4.  **停止服務**：

    ```bash
    docker-compose down
    ```

## 📄 API 文件

一旦應用程式運行，你可以在瀏覽器中訪問以下 URL 來查看互動式 API 文件：

  * **Swagger UI**：`http://localhost:8000/docs`
  * **ReDoc**：`http://localhost:8000/redoc`

## 💡 API 端點範例

以下是一些常見的 API 操作範例（使用 `curl`）。請替換 `your_access_token` 和其他佔位符。

### 1\. 會員註冊

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

### 2\. 會員登入 (獲取 JWT)

```bash
curl -X POST "http://localhost:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=newuser&password=strongpassword123"
# 響應會包含 access_token，請儲存此 token 以用於後續的認證請求
```

### 3\. 獲取當前使用者資訊 (需要認證)

假設你已從登入請求中獲取到 `access_token`。

```bash
curl -X GET "http://localhost:8000/users/me" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 4\. 更新當前使用者資訊 (需要認證)

```bash
curl -X PUT "http://localhost:8000/users/me" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "full_name": "Updated Name",
  "phone_number": "0987654321"
}'
```

### 5\. 為當前使用者新增送貨地址 (需要認證)

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

## 部署

### 本地部署

推薦使用 `uvicorn` 直接運行：

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 生產環境建議

在生產環境中部署時，請考慮以下最佳實踐：

  * **資料庫**：強烈建議使用 **PostgreSQL** 或 **MySQL** 替代 SQLite，以提升性能、可靠性、併發處理能力和資料持久性。更新 `DATABASE_URL` 環境變數即可。
  * **密鑰安全**：確保 `SECRET_KEY` 是一個強大且安全的隨機字串。你可以使用以下 Python 命令生成：
    ```bash
    python -c "import secrets; print(secrets.token_hex(32))"
    ```
  * **環境變數管理**：使用環境變數（如 Docker `environment` 或 Kubernetes `secrets`）而非硬編碼敏感資訊。
  * **反向代理**：使用 Nginx 或 Caddy 等反向代理伺服器來處理 HTTPS (SSL/TLS)、負載均衡和靜態檔案服務。
  * **應用伺服器**：使用 `Gunicorn` 運行多個 `Uvicorn` 工作進程，以充分利用多核 CPU 並提高併發處理能力：
    ```bash
    gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000
    ```
    這裡 `-w 4` 表示運行 4 個工作進程，`-k uvicorn.workers.UvicornWorker` 指定 Uvicorn 的 worker 類型。
  * **日誌和監控**：配置適當的日誌記錄機制（例如使用 ELK Stack 或 Grafana Loki）和監控工具（如 Prometheus、Grafana）來追蹤應用程式的性能和健康狀況。

### Docker 部署

通過 Docker Compose 可以快速部署整個應用：

1.  確保 `docker-compose.yaml` 中的環境變數（尤其是 `SECRET_KEY` 和 `DATABASE_URL`）已正確配置或通過 `.env` 文件提供。
2.  在專案根目錄運行：
    ```bash
    docker-compose up --build -d
    ```
    應用程式將在 Docker 容器中運行，映射到主機的 8000 埠。

## 🔮 未來改進與擴展

此專案為基礎，未來可以朝以下方向進行擴展和優化：

  * **電子郵件服務整合**：
      * 實現真實的電子郵件發送功能，用於帳戶啟用、電子郵件驗證、密碼重設連結等。
      * 整合郵件發送服務（如 SendGrid, Mailgun, AWS SES）。
  * **完整密碼重設流程**：
      * 實現安全的密碼重設 Token 管理（獨立於 JWT），確保 Token 的時效性和單次使用。
  * **會員等級與積分系統**：
      * 新增會員等級模型，基於用戶行為（如消費金額、訂單數量）自動升級。
      * 實現積分增減、查詢和使用功能。
  * **購物車功能**：
      * 建立購物車模型，支持添加、更新、刪除商品。
      * 與商品庫存管理整合。
  * **訂單管理**：
      * 實現訂單創建、查詢、更新狀態（待支付、已支付、已發貨、已完成等）。
      * 支援多個商品和多個地址的訂單關聯。
  * **支付閘道器整合**：
      * 與常見的支付服務（如 Stripe, PayPal, Line Pay, 綠界）進行整合，處理交易。
  * **後台管理介面**：
      * 基於管理員權限，提供一個 Web 介面來管理使用者、訂單、地址等資料。
      * 可以考慮使用 [FastAPI-Admin](https://github.com/fastapi-admin/fastapi-admin) 或自行開發。
  * **單元測試和整合測試覆蓋率**：
      * 增加更多的測試用例，提高測試覆蓋率，確保程式碼的穩定性和可靠性。
  * **異步任務處理**：
      * 對於耗時的操作（如發送郵件、生成報告），可以整合 Celery 或 Dramatiq 等任務佇列來異步處理，避免阻塞 API 響應。
  * **更詳細的日誌記錄**：
      * 實現結構化日誌，並集成到日誌管理系統。
  * **API 限流 (Rate Limiting)**：
      * 防止惡意請求或濫用 API，可以集成 `fastapi-limiter`。
  * **資料庫遷移工具**：
      * 使用 `Alembic` 來管理資料庫 Schema 的變更。

-----

## 許可證

此專案根據 MIT 許可證發布。詳情請參閱 [LICENSE](https://www.google.com/search?q=LICENSE) 文件。

```
```