# 🚀 FastAPI Object Detection API  

This project is a **RESTful API** for managing customers and addresses, following REST best practices. The API is built using **FastAPI (Python)**, with **MariaDB** as the database and **Docker** for containerized deployment.

---

---

## 📌 Features
✅ **RESTful API**: Follows standard RESTful guidelines.  
✅ **Request Validation**: Ensures data integrity with proper validation.  
✅ **Database Migration**: Uses Alembic (Python).
✅ **Unit Tests**: Implements test cases for all endpoints.  
✅ **Elegant Error Handling & Logging**: Logs errors with structured logging.  
✅ **Docker Support**: Runs in a containerized environment.  
✅ **Swaggers UI**: /docs

---

## 🛠 Tech Stack
- **FastAPI** – API framework  
- **MariaDB** – Database  
- **SQLAlchemy** – ORM  
- **Alembic** – Database migrations  
- **Pytest** – Unit testing  
- **Docker & Docker Compose** – Containerized deployment


---

## 📂 Project Structure
```plaintext
📦 fastapi-object-detection
 ┣ 📂 src
 ┃ ┣ 📂 api           # API routes
 ┃ ┣ 📂 core          # Configurations & settings
 ┃ ┣ 📂 models        # ORM
 ┃ ┣ 📂 services      # Business logic CRUD / repository
 ┃ ┣ 📂 routes        # Routing
 ┃ ┣ schemas        # Serializer
 ┃ ┣ 📜 main.py       # FastAPI app entry point
 ┣ 📂 test           # Unit and integration tests
 ┣ 📜 docker-compose.yml  # Docker services configuration
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 README.md           # Documentation
```

---

## 🛠 Installation & Setup

### 🔹 1. Non-docker
```sh
git clone https://github.com/farhanfadillahr/fastapi_psn.git
cd fastapi_psn
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
fastapi run src/main.py --port 8000
```

### 🔹 2. Using docker
```sh
docker compose up
```

## Installation & Setup


