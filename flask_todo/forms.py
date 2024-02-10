from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired,Length
        

class TodoForm(FlaskForm):
    todo = TextAreaField('Title', validators=[DataRequired()], render_kw={
        'class':'bg-black shadow appearance-none outline-none border-2 border-gray-800 focus:border-2 focus:border-gray-400 rounded-xl w-full py-2 px-3 text-white',
        'placeholder': "write something..."
    })