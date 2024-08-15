from django.db import models
from django.contrib.auth.models import User
from datetime import *

class Customers(models.Model):
	address = models.TextField()
	contact = models.BigIntegerField()
	gender = models.CharField(max_length=10)
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'customers'

class Inquiry(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	contact = models.BigIntegerField()
	subject = models.CharField(max_length=50)
	message = models.TextField()

	class Meta:
		db_table = 'inquiry'

class Feedback(models.Model):
	rate = models.CharField(max_length=20)
	comment = models.TextField()
	customers = models.OneToOneField(Customers,on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)

	class Meta:
		db_table = 'feedback'

class State(models.Model):
	states = models.CharField(max_length=150)

	class Meta:
		db_table = 'state'

class City(models.Model):
	cities = models.CharField(max_length=150)
	state = models.ForeignKey(State,on_delete=models.CASCADE)

	class Meta:
		db_table = 'city'

class Company(models.Model):
	agency_name = models.CharField(max_length=255)
	contact = models.BigIntegerField()
	establish_date = models.DateField()
	address = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	cur_date = models.DateField(default=date.today)
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		db_table = 'company'

class Add_new_ad_type(models.Model):
	size = models.CharField(max_length=255)
	page_no = models.CharField(max_length=100)
	description = models.TextField(max_length=255)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	mode = models.CharField(max_length=30)
	image_name = models.CharField(max_length=255)
	company = models.ForeignKey(Company,on_delete=models.CASCADE)

	class Meta:
		db_table = 'add_new_ad_type'

class Order(models.Model):
	size = models.CharField(max_length=100)
	page_no = models.CharField(max_length=100)
	mode = models.CharField(max_length=100)
	order_date = models.DateField()
	date = models.DateField(default=date.today)
	subject = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	customers = models.ForeignKey(Customers,on_delete=models.CASCADE,default=None)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,default=None)

	class Meta:
		db_table = 'order'
