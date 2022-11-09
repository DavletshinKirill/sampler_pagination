from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    title = StringField("Enter a book", validators=[DataRequired(), Length(1, 30)])
    author = StringField("Enter the book's Author", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("Log In")
