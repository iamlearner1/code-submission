# FAQ API - Backend Developer Intern Project

## Overview
This project is a **Django REST Framework (DRF) API** for managing FAQs (Frequently Asked Questions). It includes:
- A **REST API** for fetching FAQs.
- **Django Admin Panel** for managing FAQs.
- **Redis** for request handling and caching.
- **Dockerized Setup** for easy deployment.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL / SQLite
- **Cache**: Redis
- **Containerization**: Docker, Docker Compose

## Features
- **Retrieve FAQs** via API.
- **Admin Panel** for managing FAQs.
- **Redis** integration for request handling.

## Installation

### 1. Clone the Repository
```sh
$ git clone https://github.com/iamlearner1/code-submission.git
$ cd faq_project
```

### 2. Create & Activate Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Mac/Linux
$ venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
$ python manage.py migrate
```

### 5. Create Superuser
```sh
$ python manage.py createsuperuser
```

### 6. Run the Server
```sh
$ python manage.py runserver
```
Now, visit **http://127.0.0.1:8000/admin/** to log in and add FAQs.

## API Endpoints
| Method | Endpoint       | Description           |
|--------|--------------|----------------------|
| GET    | `/api/faq/`  | Retrieve all FAQs    |

You can use **Postman** or any API testing tool to fetch FAQs.

## Running with Docker

### 1. Build the Docker Image
```sh
$ docker build -t mydjangoapp .
```

### 2. Run the Project with Docker Compose
```sh
$ docker-compose up
```

Now, visit **http://127.0.0.1:8000/** to access the project.

## Redis Setup
Ensure Redis is running before starting the project. If not installed, install Redis:
```sh
$ sudo apt install redis-server  # Linux
$ brew install redis  # macOS
```
Start Redis:
```sh
$ redis-server
```

## Deployment
For production, set up **Gunicorn** and **NGINX** or use cloud platforms like AWS, Heroku, or DigitalOcean.

---
This project demonstrates:
✅ **API Development with Django & DRF**  
✅ **Efficient Request Handling with Redis**  
✅ **Containerization using Docker**  
✅ **Admin Panel for Managing Data**  

## About Me
I have knowledge of **Django**, but this is my first complete project using it. I also know how to build APIs using **Spring Boot, JPA, TypeScript, and GraphQL**. While learning Django REST Framework (DRF), I found it extremely useful and fast for creating REST APIs. I look forward to learning more and enhancing my skills further.

I am very interested in this opportunity and believe it will help me grow as a developer. You can check out my GitHub profile for more projects: [GitHub Profile](http://github.com/iamlearner1).

I want to be transparent with you—I used **ChatGPT** to assist me in completing this project. However, I fully understand the code and can explain it without AI assistance. I believe AI helps improve code efficiency and reduces development time, but I am confident in my ability to complete projects independently as well.

Hope you find this project useful! 🚀

