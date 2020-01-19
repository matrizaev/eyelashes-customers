from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
import uuid
import qrcode
import qrcode.image.svg
from xml.etree.ElementTree import tostring
from flask import url_for
import io
from datetime import datetime

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
	
class User(UserMixin, db.Model):
	id  = db.Column(db.Integer, primary_key = True)
	email	= db.Column(db.String(120), index = True, unique = True, nullable=False)
	password = db.Column(db.String(128), nullable=False)
	customers = db.relationship('Customer', backref = 'user')
	
	def __repr__ (self):
		return '<User {}>'.format(self.email)
	
	def SetPassword(self, password):
		self.password = generate_password_hash(password)
		
	def CheckPassword(self, password):
		return check_password_hash(self.password, password)
		
	def GetAvatar(self, size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Customer(db.Model):
	first_name = db.Column(db.String(128), nullable=True)
	last_name = db.Column(db.String(128), nullable=True)
	phone = db.Column(db.String(128), nullable=True)
	guid = db.Column(db.String(128), primary_key = True, default = str(uuid.uuid4()))
	qr_code = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	discount = db.Column(db.Integer, nullable=False, default=10, server_default='10')
	visit_count = db.Column(db.Integer, nullable=False, default = 10, server_default='10')
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	
	def GenerateQRcode(self):
		img = qrcode.make(url_for('main.ShowIndex', _anchor=self.guid, _external=True), image_factory=qrcode.image.svg.SvgPathFillImage, box_size=10)
		stream = io.BytesIO()
		img.save(stream)
		stream.seek(0)
		self.qr_code = stream.read().decode('utf-8')
	
