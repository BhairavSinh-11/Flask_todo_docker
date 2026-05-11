# 🚀 Flask To-Do App — Dockerized & Deployed on AWS

A containerized Flask To-Do application deployed on AWS EC2 using Docker and Gunicorn.

---

## 🐳 Docker Features

✅ Dockerized Flask application
✅ Custom Dockerfile setup
✅ Volume mounting for development
✅ Port mapping configuration
✅ Production-ready container setup using Gunicorn

---

## ☁️ AWS Deployment

This project was successfully deployed on:

* ☁️ AWS EC2
* 🐧 Amazon Linux
* 🔐 SSH Remote Access
* 🛡️ AWS Security Groups
* 🐳 Docker Engine

---

## ⚙️ Deployment Workflow

```text id="1h2ll2"
Local Flask App
        ↓
Docker Image
        ↓
Docker Container
        ↓
AWS EC2 Instance
        ↓
Live Application
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 🌶️ Flask
* 🐳 Docker
* 🔫 Gunicorn
* ☁️ AWS EC2
* 🐧 Linux

---

## 📦 Docker Commands Used

### Build Docker Image

```bash id="yn2u3k"
docker build -t flask-docker .
```

### Run Docker Container

```bash id="z7m4vd"
docker run -d -p 2423:2423 -v $(pwd):/app --name flask_docker flask-docker
```

---

## 🔐 AWS Security Configuration

Configured inbound rules for:

* SSH (22)
* HTTP (80)
* Custom Flask Port (2423)

---

## 📖 What I Learned

* Building Docker images
* Managing Docker containers
* Volume mounting in Docker
* Running Flask with Gunicorn
* Deploying containers on AWS EC2
* Linux server management
* SSH configuration & remote deployment

---

⭐ This project helped me understand real-world containerized deployment workflows using Docker and AWS.
