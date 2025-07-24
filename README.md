# 🤖 Flask Microservice – Programming Jokes API

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Docker](https://img.shields.io/badge/Deployed-Docker-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

A Flask-based microservice that returns programming jokes based on humor level and selected language.  
This version includes a PostgreSQL database that is automatically populated when the container starts.

---

## 🚀 Tech Stack

- Python + Flask
- PostgreSQL
- Docker & Docker Compose

---

## 🧩 Features

- ✅ Filter jokes by humor level (`low`, `medium`, `high`)
- ✅ Language selection via `Accept-Language` header (`en-us` / `pt-br`)
- ✅ Fully containerized with Docker
- ✅ Automatic table creation and joke insertion on container start

---

## ⚙️ How to Run Locally

### Prerequisites

- Docker
- Docker Compose

### Setup

```bash
git clone <REPOSITORY_URL>
cd flask-microservice
docker-compose up --build
```

The API will run on http://localhost:5000

📡 API Endpoint
GET /joke
Returns a programming joke based on the query and headers.

Query Parameters
level=low | medium | high

Headers
Accept-Language: en-us for English

Accept-Language: pt-br for Portuguese

```bash
curl --location 'http://localhost:5000/joke?level=low' \
--header 'Accept-Language: pt-br'
```


![image](https://github.com/user-attachments/assets/3d95d22e-f20d-4978-9dfa-45f666f196a6)
