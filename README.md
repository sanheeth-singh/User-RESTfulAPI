# User Management API

A robust, lightweight RESTful API designed to demonstrate professional backend architecture. This project implements full **CRUD** (Create, Read, Update, Delete) operations for user data, featuring a modular codebase and a built-in interactive documentation dashboard.

## 📖 Description

This API serves as a backend foundation for managing user identities. Unlike simple script-based APIs, this project uses a **refactored architecture** that separates database models, API resources, and application configuration. It includes a custom-built "Claymorphism" landing page that acts as self-hosting documentation for developers.

## 🛠️ Tech Stack

* **Core Framework:** Python 3.x, Flask
* **API Extension:** Flask-RESTful (Class-Based Resources)
* **Database:** SQLite & SQLAlchemy ORM
* **Validation:** ReqParser (Input validation) & Marshal (Output serialization)
* **Frontend:** HTML5, CSS3 (Claymorphism Design)

## ✨ Features

* **Full CRUD Capabilities:** Create, Read, Update (Partial PATCH), and Delete users.
* **Modular Architecture:** Codebase split into `models.py`, `resources.py`, and `app.py` for scalability.
* **Input Validation:** Automatic handling of missing or malformed data using `reqparse`.
* **Data Serialization:** Secure data formatting using `@marshal_with` to control API responses.
* **Interactive Dashboard:** A built-in web page (`/`) running on the server to document endpoints and usage.
* **Database Management:** Automatic initialization of SQLite database tables.

## ⚙️ Installation & Setup

Follow these steps to run the API locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/project-name.git](https://github.com/YOUR_USERNAME/project-name.git)
cd project-name
```
### 2. Create a Virtual Environment (Recommended)
# Windows
```bash 
python -m venv venv
venv\Scripts\activate
```

# Mac/Linux
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install flask flask-restful flask-sqlalchemy
```
# OR if you created a requirements file:
```
pip install -r requirements.txt
```

### 4. Run The Application 
``` 
python api.py
```
## API Endpoints
Use tools like Postman or Thunder Client to test these routes:
| Method | Endpoint            | Description         | Payload (JSON)                         |
|--------|---------------------|---------------------|----------------------------------------|
| GET    | `/api/users/`       | Fetch all users     | N/A                                    |
| POST   | `/api/users/`       | Create a user       | `{ "name": "...", "email": "..." }`    |
| GET    | `/api/users/<id>`   | Fetch single user   | N/A                                    |
| PATCH  | `/api/users/<id>`   | Update user         | `{ "name": "..." }`                    |
| DELETE | `/api/users/<id>`   | Delete user         | N/A                                    |
