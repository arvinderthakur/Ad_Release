from django.shortcuts import render,redirect
from myadmin.models import *
from django.contrib.auth.models import auth,User

# Create your views here.

def dashboard(request):
	context = {}
	return render(request, 'myadmin/dashboard.html', context)

def login(request):
	context = {}
	return render(request, 'myadmin/login.html', context)

def login_check(request):
	username = request.POST['email-username']
	password = request.POST['password']	

	result = auth.authenticate(request, username=username , password=password)

	if result is None:
		print('Invalid username or password')
		return redirect('/myadmin/')

	else:
		if result.is_superuser:
			auth.login(request, result)
			return redirect('/myadmin/dashboard')

		else:
			print('Invalid username or password')
			return redirect('/myadmin/')

def register(request):	
	context = {}
	return render(request, 'myadmin/register.html', context)

def add_state(request):
	context = {}
	return render(request, 'myadmin/add_state.html', context)

def state_store(request):
	mysname    = request.POST['states']

	State.objects.create(states=mysname)
	return redirect('/myadmin/add_state')

def all_states(request):
	result = State.objects.all()
	context = {'result':result}
	return render(request,'myadmin/all_states.html',context)

def add_city(request):
	result = State.objects.all()
	context = {'result': result}
	return render(request, 'myadmin/add_city.html', context)

def city_store(request):
	mycity  = request.POST['city']
	mystateid    = request.POST['states']

	City.objects.create(cities=mycity,state_id=mystateid)
	return redirect('/myadmin/add_city')

def view_location(request):
	result = State.objects.all()
	context = {'result': result}
	return render(request, 'myadmin/view_location.html', context)

def view_city(request,id):
	result = State.objects.get(pk=id)
	state_id = result.id
	result1 = City.objects.filter(state_id=state_id)
	context = {'result1':result1}
	return render(request, 'myadmin/view_city.html', context)

def add_agency(request):
	result = State.objects.all()
	# st_id = result.State.id
	result1 = City.objects.all()
	context = {'result': result,'result1':result1}
	return render(request, 'myadmin/add_agency.html', context)

def add_agency_store(request):
	# User model

	firstname = request.POST['fname']
	lastname = request.POST['lname']
	email = request.POST['email']
	username = request.POST['username']
	password = request.POST['password']
	cpassword = request.POST['cpassword']

	# Company model

	agency_name = request.POST['agency_name']
	contact = request.POST['contact']
	establishdate = request.POST['establishe_date']
	address = request.POST['address']
	city = request.POST['city']
	state = request.POST['states']

	if password == cpassword :
		result = User.objects.create_user(email=email,first_name=firstname,last_name=lastname,username=username,password=password)
		Company.objects.create(agency_name=agency_name,contact=contact,establish_date=establishdate,address=address,city_id=city,state_id=state,user_id=result.id)
		return redirect('/myadmin/add_agency')

	else :
		print('Password and Confirm password is not same')
		return redirect('/myadmin/msg')

def msg(request):	
	context = {}
	return render(request, 'myadmin/msg.html', context)

def agency(request):
	result = Company.objects.all()
	context = {'result' : result}
	return render(request, 'myadmin/agency.html', context)
	
def view_agency(request,id):
	result = Company.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'myadmin/view_agency.html', context)

def customers(request):
	result = Customers.objects.all()
	context = {'result' : result}
	return render(request, 'myadmin/customers.html', context)

def view_customers(request,id):
	result = Customers.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'myadmin/view_customers.html', context)
	
def orders(request):
	oresult = Order.objects.all()
	context = {'result' : oresult}
	return render(request, 'myadmin/orders.html', context)

def inquiry(request):
	result = Inquiry.objects.all()
	context = {'result' : result}
	return render(request, 'myadmin/inquiry.html', context)

def feedback(request):
	fresult = Feedback.objects.all()
	context = {'result' : fresult}
	return render(request, 'myadmin/feedback.html', context)

def form(request):
	context = {}
	return render(request, 'myadmin/form.html', context)

def table(request):
	context = {}
	return render(request, 'myadmin/table.html', context)