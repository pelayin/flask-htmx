from app import db


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    books = db.relationship("Book", backref="author", lazy=True)

    def __repr__(self):
        return f"<Author {self.name}>"


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"))

    def __repr__(self):
        return f"<Book {self.title}>"
