📘 Introduction
Book Summary Translator is a web application that allows users to view book summaries and translate them into multiple languages. It uses:
•	A simple frontend built with HTML & JavaScript
•	Two Flask backend services for book data and translation (via MyMemory API)
•	Docker Compose to easily manage and run the app
This app demonstrates how to integrate APIs, build a multilingual system, and orchestrate containers.


📑 Table of Contents
 •	Introduction

•	Prerequisites

•	How to Run the App

•	Access the App

•	API Endpoints

•	How it works

•	Technologies Used

•	Authors


## ✅ Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 How to Run the App

Open a terminal in the project root folder and run:

```bash
docker-compose up --build
```

🌐 Access the App
Once the containers are running, you can access the app at:

🖥 Frontend UI	
http://localhost:8080

📘 Book API
	http://localhost:8081/books

🌍 Translation API	
http://localhost:5000/Summary/1

🔌 API Endpoints
📘 Book API (http://localhost:8081)

•	GET /books → Get list of all books

•	GET /books/<id> → Get book by ID

🌍 Translate API (http://localhost:5000)

•	GET /Summary/<book_id> → Get the original summary

•	GET /Translate/<book_id>?language=<lang> → Get translated summary

⚙️ How It Works

Frontend allows users to:

•	Select a book

•	View the original summary

•	 Choose a language to translate

•	 Serves book data from summaries.json

•	Calls MyMemory Translation API to translate the summary

•	Ties all services together in isolated containers with shared networking


🛠 Technologies Used

•	Backend: Python (Flask)

•	Frontend: HTML, CSS, JavaScript

•	Translation API: MyMemory (free)

•	DevOps: Docker & Docker Compose

•	Web Server: Nginx (for serving frontend)

👨‍💻 Authors

•	Sushma Katakam

