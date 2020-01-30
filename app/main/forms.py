from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, StringField, BooleanField, FloatField, TextAreaField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError, InputRequired, NumberRange

class AddCustomerForm(FlaskForm):
	count = IntegerField('Количество', render_kw={'type': 'number', 'step':'any', 'value':10, 'min':1}, validators = [DataRequired(message='Количество - обязательное поле.'), NumberRange(min=1, message='Невозможно добавить меньше одного клиента.')])
	discount = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'value':10}, validators = [InputRequired(message='Скидка - обязательное поле.')])
	submit = SubmitField('Сохранить')

class EditCustomerForm(FlaskForm):
	guid = StringField('Идентификатор', validators = [DataRequired(message='Идентификатор - обязательное поле.')])
	first_name = StringField('Имя')
	last_name = StringField('Фамилия')
	phone = StringField('Телефон')
	visit_count = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any', 'min':0}, validators = [InputRequired(message='Счётчик посещений - обязательное поле.'), NumberRange(min=0, message='Посещения не могут быть меньше нуля.')])
	discount = IntegerField('Скидка', render_kw={'type': 'number', 'step':'any'}, validators = [InputRequired(message='Скидка - обязательное поле.')])