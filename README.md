
# 📌 Project Management API

A **RESTful backend API for managing organizations, projects, and tasks**.
This system allows users to create organizations, manage members, create projects, and track tasks within those projects.

The API includes **JWT authentication, pagination, searching, sorting, and filtering** to simulate real-world backend development practices.

---

# 🚀 Features

* 🔐 **JWT Authentication**
* 👤 **User Management**
* 🏢 **Organization Management**
* 👥 **Organization Member Roles**
* 📂 **Project Management**
* ✅ **Task Management**
* 🔎 **Search functionality**
* 📊 **Pagination & Limit**
* ↕️ **Sorting**
* 🧩 **RESTful API Design**

---

# 🏗️ Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy ORM**
* **PostgreSQL**
* **JWT Authentication**
* **Pydantic**
* **Uvicorn**

---

# 📂 Database Models

## User

Stores application users.

| Field    | Type            |
| -------- | --------------- |
| id       | Integer         |
| name     | String          |
| email    | String (Unique) |
| password | String          |

---

## Organization

Represents a company/team.

| Field       | Type      |
| ----------- | --------- |
| id          | Integer   |
| name        | String    |
| status      | String    |
| description | Text      |
| createdAt   | Timestamp |
| updatedAt   | Timestamp |

---

## OrganizationMember

Defines which users belong to an organization.

| Field           | Type                          |
| --------------- | ----------------------------- |
| id              | Integer                       |
| user_id         | ForeignKey (users.id)         |
| organization_id | ForeignKey (organizations.id) |
| role            | String                        |

---

## Project

Projects created under organizations.

| Field          | Type                          |
| -------------- | ----------------------------- |
| id             | Integer                       |
| name           | String                        |
| organizationId | ForeignKey (organizations.id) |
| status         | String                        |
| description    | Text                          |
| createdAt      | Timestamp                     |
| updatedAt      | Timestamp                     |

---

## Task

Tasks belonging to projects.

| Field       | Type                     |
| ----------- | ------------------------ |
| id          | Integer                  |
| title       | String                   |
| project_id  | ForeignKey (projects.id) |
| assigned_to | ForeignKey (users.id)    |
| status      | String                   |
| priority    | String                   |
| description | Text                     |
| createdAt   | Timestamp                |
| updatedAt   | Timestamp                |

---

# 🔐 Authentication

The API uses **JWT (JSON Web Token)** authentication.

Steps:

1️⃣ Register a user
2️⃣ Login to get a **JWT access token**
3️⃣ Use the token in request headers

```
Authorization: Bearer <your_token>
```

---

# 📡 API Features

### Pagination

Control the number of results returned.

```
GET /tasks?page=1&limit=10
```

---

### Search

Search resources using query parameters.

```
GET /projects?search=inventory
```

---

### Sorting

```
GET /tasks?sort_by=createdAt&order=desc
```

---

# 📁 Project Structure

```
project-management-api
│
├── app
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── routers
│   │     ├── users.py
│   │     ├── organizations.py
│   │     ├── projects.py
│   │     └── tasks.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/project-management-api.git
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

---

# 📬 API Documentation

FastAPI automatically generates documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📈 Future Improvements

* Role-based access control
* Task comments
* File attachments
* Activity logs
* Notifications
* Docker deployment

---

# 👨‍💻 Author

**Rakesh N**

Backend Developer
Skilled in **Python, FastAPI, Django, SQLAlchemy**
