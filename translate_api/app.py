from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

LIBRARY_API="http://book_api:81/books"

Translate_API="https://api.mymemory.translated.net/get?q={}&langpair=en|{}"

@app.route('/Translate/<int:book_id>')
def translate(book_id):
    urlLibrary=LIBRARY_API
    language = request.args.get("language", "en")
    responseBooks = requests.get(urlLibrary).json()
    book = next((b for b in responseBooks if b['id'] == book_id), None)
    if book:
        summary=book["summary"]
        title=book["title"]
    if language == "":    
        language="fr"
        
    urlTranslate = Translate_API.format(summary,language)
    responseTr=requests.get(urlTranslate).json()
    return jsonify(title ,summary, responseTr["matches"][0]["translation"] if "matches" in responseTr else "Translation failed." ,)


@app.route('/Summary/<int:book_id>')
def summary(book_id):
    urlLibrary=LIBRARY_API
    responseBooks = requests.get(urlLibrary).json()
    book = next((b for b in responseBooks if b['id'] == book_id), None)
    if book:
        summary=book["summary"]
    return (summary)




@app.route('/')
def home():
    return "This is an api for translating summaries of books from the Books api. Please provide the URL with book ID and language"


# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
