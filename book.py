from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    publisher = db.Column(db.String(80), unique=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher} - {self.id}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    book = Book.query.all()

    output = []
    for book in book:
        book_data = {'id': book.id, 'book_name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"id": book.id, "book_name": book.name, "author": book.author, "publisher": book.publisher})

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['ISBN'], book_name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': drink.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted!"}