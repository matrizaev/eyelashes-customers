from app import db
from app.models import Customer
from flask import redirect, flash, render_template, request, url_for, Response, jsonify
from flask_login import current_user, login_required
from app.main import bp
from app.main.forms import AddCustomerForm, EditCustomerForm
import uuid

@bp.route('/')
@bp.route('/index/')
@login_required
def ShowIndex():
	add_form = AddCustomerForm()
	edit_form = EditCustomerForm()
	return render_template('index.html', add_form = add_form, edit_form = edit_form)
	
@bp.route('/qrcode/<guid>')
@login_required	
def ShowQRcode(guid):
	customer = Customer.query.filter(Customer.guid == guid, Customer.user_id == current_user.id).first()
	if customer:
		return Response (customer.qr_code, mimetype='image/svg+xml', headers = {'Content-Disposition':'attachment;filename={}.svg'.format(guid)})
	else:
		flash('Клиент не найден')
		return redirect(url_for('main.ShowIndex'), code = 302)
	
@bp.route('/add', methods=['POST'])
@login_required
def AddCustomer():
	form = AddCustomerForm(request.form)
	if form.validate_on_submit():
		for i in range(form.count.data):
			customer = Customer(guid = str(uuid.uuid4()), discount = form.discount.data, visit_count = form.visit_count.data)
			customer.GenerateQRcode()
			current_user.customers.append(customer)
			db.session.add(customer)
		db.session.commit()
		flash('Клиенты успешно добавлен')
	else:
		for error in form.count.errors + form.discount.errors:
			flash(error)
	return redirect(url_for('main.ShowIndex'))	
	
@bp.route('/edit', methods=['POST'])
@login_required
def EditCustomer():
	flashMessages = list()
	status = False
	form = EditCustomerForm(request.form)
	if form.validate_on_submit():
		customer = Customer.query.filter(Customer.guid == form.guid.data, Customer.user_id == current_user.id).first()
		if customer:
			if form.visit_count.data == 0:
				db.session.delete(customer)
				flashMessages.append('Клиент удалён, посещения истекли.')
			else:
				customer.first_name = form.first_name.data
				customer.last_name = form.last_name.data
				customer.phone = form.phone.data
				customer.discount = form.discount.data
				customer.visit_count = form.visit_count.data
				flashMessages.append('Клиент успешно изменён')
			db.session.commit()
			status = True
		else:
			flashMessages.append('Клиент не найден')
	else:
		for error in form.first_name.errors + form.last_name.errors + form.phone.errors + form.discount.errors + form.guid.errors + form.visit_count.errors:
			flashMessages.append(error)
	if not status and len(flashMessages) == 0:
		flashMessages.append('Не удалось внести изменения')
	return jsonify({'status':status, 'flash':flashMessages})
	