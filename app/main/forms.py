from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, StringField, BooleanField, FloatField, TextAreaField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError, Length

class AddCustomerForm(FlaskForm):
	first_name = StringField('Имя', validators = [DataRequired(message='Имя - обязательное поле.')])
	last_name = StringField('Фамилия', validators = [DataRequired(message='Фамилия - обязательное поле.')])
	phone = StringField('Телефон')
	discount = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'value':0})
	submit = SubmitField('Сохранить')

class EditCustomerForm(FlaskForm):
	guid = StringField('Идентификатор', validators = [DataRequired(message='Идентификатор - обязательное поле.')])
	first_name = StringField('Имя', validators = [DataRequired(message='Имя - обязательное поле.')])
	last_name = StringField('Фамилия', validators = [DataRequired(message='Фамилия - обязательное поле.')])
	phone = StringField('Телефон')
	visit_count = IntegerField('Скидка', validators = [DataRequired(message='Счётчик посещений - обязательное поле.')])
	discount = IntegerField('Скидка', validators = [DataRequired(message='Скидка - обязательное поле.')])