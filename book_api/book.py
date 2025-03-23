from flask import Flask, jsonify
from flask_cors import CORS
import json


# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Load book summaries data
with open("summaries.json", "r") as f:
    books_data = json.load(f)

# Define a route to get all book summaries
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books_data)

# Define a route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books_data if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=81)
