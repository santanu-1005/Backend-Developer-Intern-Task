# Backend-Developer-Intern-Task

# 📊 Dataset Catalog API

This project is a simple backend API using **Python**, **Flask**, and **MongoDB**, simulating a lightweight Dataset Catalog. Users can manage datasets and attach quality logs (PASS or FAIL), all stored in MongoDB.

---

## ✅ Features

- CRUD operations for datasets
- Add/view quality logs per dataset
- Soft delete support
- Filtering by dataset owner or tag
- Schema validation using Pydantic
- Swagger UI documentation with Flasgger
- Unit testing with `pytest`

---

## 🧰 Tech Stack

- Python 3.10+
- Flask 2.x
- MongoDB
- PyMongo
- Pydantic
- Flasgger (Swagger)

---

## 📁 Project Structure
```bash
├── app.py # Main Flask application
├── models/
│ ├── schema.py # Pydantic models for request validation
├── routes/
│ └── dataset_route.py # Flask route definitions
├── services/
│   ├── dataset_service.py
│   └── quality_log_service.py
├── requirements.txt
└── README.md
```
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/santanu-1005/Backend-Developer-Intern-Task.git
cd Backend-Developer-Intern-Task
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate          # On Windows
# OR
source venv/bin/activate       # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run The Flask App
```bash
# For Windows
set FLASK_APP=app.py
flask run

# For macOS/Linux
export FLASK_APP=app.py
flask run
```
## 📌 API Endpoints

| Method | Route                         | Description                         |
|--------|-------------------------------|-------------------------------------|
| POST   | /datasets                     | Create a new dataset                |
| GET    | /datasets                     | List all datasets (filter optional) |
| GET    | /datasets/<id>                | Get dataset details                 |
| PUT    | /datasets/<id>                | Update dataset                      |
| DELETE | /datasets/<id>                | Soft delete dataset                 |
| POST   | /datasets/<id>/quality-logs   | Add quality log                     |
| GET    | /datasets/<id>/quality-logs   | View quality logs                   |

