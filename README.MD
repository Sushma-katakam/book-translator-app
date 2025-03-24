# This is a full stack dockerized application that fetches book summaries and translate them in to different languages using public APIs. 
 It includes:
•	A frontend dashboard(HTML + Js)
•	A Book Summary API(Flask)
•	A Translation API(FLASK)
•	A Translation API(Flask,uses MYMemory)
•	All Containerized and orchestrated with Docker Compose

# Prerequisites:
•	Docker
•	Docker Compose
# Run the App
docker-compose up --build

# Access the App in Browser
•	Frontend- http://localhost:8080
•	Book API - http://localhost:8081/books
•	Translation API - http://localhost:5000/Summary/1
# How It Works
Frontend allows users to:
•	Select a book
•	View the original summary
•	Choose a language to translate
•	Book API serves book data from summaries.json
•	Translate API calls MyMemory API to translate the summary
•	Docker Compose ties it all together


# API EndPoints
Book API (Port 8081)
•	GET /books – Returns list of all books
•	GET /books/<id> – Returns specific book data
Translate API (Port 5000)
•	GET /Summary/<book_id> – Returns original summary
•	GET /Translate/<book_id>?language=<lang> – Translates summary

