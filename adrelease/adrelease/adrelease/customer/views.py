from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from customer.models import *
from agency.models import *
from myadmin.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt

def home(request):
	context = {}
	return render(request, 'customer/home.html', context)

def about(request):
	context = {}
	return render(request, 'customer/about.html', context)

def contact(request):
	context = {}
	return render(request, 'customer/contact.html', context)

def register(request):
	context = {}
	return render(request, 'customer/register.html', context)

def rstore(request):
	# User model

	firstname = request.POST['fname']
	lastname = request.POST['lname']
	email = request.POST['email']
	username = request.POST['username']
	password = request.POST['password']
	cpassword = request.POST['cpassword']

	# Customer model

	contact = request.POST['contact']
	address = request.POST['address']
	gender = request.POST['gender']

	if password  == cpassword:
		result = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
		Customers.objects.create(contact=contact,address=address,gender=gender,user_id=result.id)
		return redirect('/customer/login')

	else:
		print('missmatch password')	

def login(request):
	context = {}
	return render(request, 'customer/login.html', context)

def login_check(request):
	uname = request.POST['email-username']
	passwd = request.POST['password']

	result = auth.authenticate(request, username=uname,password=passwd)

	if result is None:
		print('Invalid username or password')
		return redirect('/customer/login')

	else:
		auth.login(request, result)
		return redirect('/customer/home')

def logout(request):
	auth.logout(request)
	return  redirect('/customer/login')

def inquiry(request):
	context = {}
	return render(request, 'customer/contact.html', context)

def inquiry_store(request):
	fullname = request.POST['fname']
	email = request.POST['email']
	contact = request.POST['contact']
	subject = request.POST['subject']
	message = request.POST['message']

	Inquiry.objects.create(name=fullname,contact=contact,email=email,subject=subject,message=message)
	return redirect('/customer/contact')

def feedback(request):
	context = {}
	return render(request, 'customer/feedback.html', context)

def feedback_store(request):
	rate = request.POST['rating']
	comment = request.POST['comment']
	id = request.user.id
	customer_id = Customers.objects.get(user_id=id)
	cid = customer_id.id

	Feedback.objects.create(rate=rate,comment=comment,customers_id=cid)
	return redirect('/customer/feedback')

def post_ad(request):
	context = {}
	return render(request, 'customer/post_ad.html', context)

def select_img(request):
	context = {}
	return render(request, 'customer/select_img.html', context)

def selected_ad_types(request):
	current_size = request.POST['size']
	current_page_no = request.POST['page_no']
	current_mode = request.POST['mode']

	request.session['size'] = current_size
	request.session['page_no'] = current_page_no
	request.session['mode'] = current_mode

	result = Add_new_ad_type.objects.filter(size=current_size,page_no=current_page_no,mode=current_mode)
	context = {'result' : result}
	return render(request, 'customer/select_img.html', context)

def order(request,id):
	result = Add_new_ad_type.objects.get(pk=id)
	co_id = result.company.id
	# company_id = Company.objects.get(user_id=co_id)
	# cid = company_id.id
	request.session['company_id'] = co_id
	context = {'result' : result}
	return render(request,'customer/order.html',context)

def order_store(request,id):
	result = Add_new_ad_type.objects.get(pk=id)

	size 	= request.session['size']
	page_no = request.session['page_no']
	mode    = request.session['mode']

	image = request.FILES['image']
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(image.name, image)

	orderdate   = request.POST['odate']
	subject     = request.POST['subject']
	description = request.POST['description']

	co_id  = result.company.id
	# agency = Company.objects.get(user_id = co_id)
	# aid    = agency.id

	id   = request.user.id
	cus_id = Customers.objects.get(user_id=id)
	cid    = cus_id.id

	price  = int(result.price)
	request.session['price']=price
	
	Order.objects.create(size=size , page_no=page_no, mode=mode, order_date=orderdate, subject=subject , description=description  ,image=image, price=price, company_id=co_id,customers_id=cid )
	return redirect('/customer/payment_process')

def booking(request):
	id   = request.user.id
	cu_id = Customers.objects.get(user_id=id)
	cid    = cu_id.id

	result = Order.objects.filter(customers_id=cid)
	context = {'result' : result}
	return render(request, 'customer/booking.html', context)

def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int(request.session['price'])*100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'customer/payment_process.html',context)

@csrf_exempt
def success(request):
	context = {}
	return render(request,'customer/home.html',context)
	

