from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import DateField

from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    start_date = DateField('휴가 시작일', validators=[DataRequired()])
    end_date = DateField('휴가 종료일', validators=[DataRequired()])
    approver = StringField('승인자', validators=[DataRequired()])
