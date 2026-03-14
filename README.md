
# 📌 Project Management API

A **RESTful backend API for managing organizations, projects, and tasks** built with **FastAPI**.

The system allows teams to create organizations, manage members, create projects, and track tasks efficiently. It also integrates **AI-based task management**, where tasks are analyzed and **automatically assigned to employees based on their skill sets**.

The API implements **JWT authentication, role-based access control, pagination, searching, sorting, and filtering**, reflecting real-world backend system architecture.

---

# 🚀 Features

* 🔐 **JWT Authentication**
* 👤 **User Management**
* 🏢 **Organization Management**
* 👥 **Role-Based Access Control (Admin / Member)**
* 📂 **Project Management**
* ✅ **Task Management**
* 🤖 **AI-Based Task Assignment**
* 📊 **Project Analysis for Smart Task Distribution**
* 🔎 **Search Functionality**
* 📊 **Pagination & Limit**
* ↕️ **Sorting**
* 🧩 **RESTful API Design**
* ⚠️ **Admin Authorization for Critical Operations**

---

# 🤖 AI-Based Task Management

The system includes an **AI-powered task assignment module** that improves team productivity.

### How it works

1️⃣ Admin creates a task
2️⃣ The system analyzes **task requirements**
3️⃣ It checks **team members’ skill sets (`tech_stack`)**
4️⃣ The task is **automatically assigned to the most suitable employee**

### Benefits

* Better task distribution
* Efficient use of team skills
* Reduced manual task allocation
* Improved project productivity

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

Stores application users and their technical skills.

| Field       | Type            |
| ----------- | --------------- |
| id          | Integer         |
| name        | String          |
| email       | String (Unique) |
| password    | String          |
| designation | String          |
| tech_stack  | String          |

---

## Organization

Represents a company or team.

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

Defines which users belong to an organization and their role.

| Field           | Type                          |
| --------------- | ----------------------------- |
| id              | Integer                       |
| user_id         | ForeignKey (users.id)         |
| organization_id | ForeignKey (organizations.id) |
| role            | String (admin / member)       |

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

Tasks belonging to projects and assigned to team members.

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

### Steps

1️⃣ Register a user
2️⃣ Login to receive a **JWT access token**
3️⃣ Send the token in request headers

```
Authorization: Bearer <your_token>
```

---

# 🛡️ Authorization

The system implements **Role-Based Access Control (RBAC)**.

### Admin Permissions

* Create projects
* Create tasks
* Delete tasks
* Manage organization members

### Member Permissions

* View projects
* View assigned tasks

Admin validation is handled through a **custom dependency (`get_current_admin`)**.

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

Sort API responses.

```
GET /tasks?sort_by=createdAt&order=desc
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/project-management-api.git
```

---

### 2️⃣ Navigate to project folder

```bash
cd project-management-api
```

---

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

---

# 📬 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```
