from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, StringField, BooleanField, FloatField, TextAreaField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError, InputRequired

class AddCustomerForm(FlaskForm):
	count = IntegerField('Количество', render_kw={'type': 'number', 'step':'any', 'value':0}, validators = [DataRequired(message='Количество - обязательное поле.')])
	discount = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'value':0}, validators = [InputRequired(message='Скидка - обязательное поле.')])
	visit_count = IntegerField('Посещений', render_kw={'type': 'number', 'step':'any', 'value':0}, validators = [DataRequired(message='Счётчик посещений - обязательное поле.')])
	submit = SubmitField('Сохранить')

class EditCustomerForm(FlaskForm):
	guid = StringField('Идентификатор', validators = [DataRequired(message='Идентификатор - обязательное поле.')])
	first_name = StringField('Имя')
	last_name = StringField('Фамилия')
	phone = StringField('Телефон')
	visit_count = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'value':0}, validators = [InputRequired(message='Счётчик посещений - обязательное поле.')])
	discount = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'value':0}, validators = [InputRequired(message='Скидка - обязательное поле.')])