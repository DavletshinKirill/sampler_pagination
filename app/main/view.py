from . import main
from flask import url_for, redirect, render_template, request

from .. import db
from ..model import Book
from .form import BookForm


@main.route("/", methods=['GET', 'POST'])
def books_storage():
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=5)
    return render_template("user.html", books=books)


@main.route("/create", methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("main.books_storage"))
    return render_template("index.html", form=form, title="Create Note")

