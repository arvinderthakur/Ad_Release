from django.shortcuts import render,redirect
from myadmin.models import *
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your views here.

def dashboard(request):
	context = {}
	return render(request, 'agency/dashboard.html', context)

def login(request):
	context = {}
	return render(request, 'agency/login.html', context)

def login_check(request):
	username = request.POST['email-username']
	password = request.POST['password']

	result = auth.authenticate(request, username=username , password=password)

	if result is None:
		print('Invalid username or password')
		return redirect('/agency/login')

	else:
		auth.login(request, result)
		return redirect('/agency/dashboard')

def add_new_ad_type(request):
	context = {}
	return render(request, 'agency/add_new_ad_type.html', context)

def add_new_ad_type_store(request):
	size = request.POST['size']
	pageno = request.POST['page']
	descript = request.POST['description']
	price = request.POST['price']
	mode = request.POST['mode']
	img = request.FILES['image']

	mylocation =  os.path.join(settings.MEDIA_ROOT,'upload')
	obj =  FileSystemStorage(location=mylocation)
	obj.save(img.name,img)
	
	id = request.user.id
	company_id = Company.objects.get(user_id=id)
	cid = company_id.id

	Add_new_ad_type.objects.create(size=size,page_no=pageno,description=descript,price=price,mode=mode,image_name=img,company_id=cid)
	return redirect('/agency/add_new_ad_type')

def all_ad_types(request):
	id = request.user.id
	company_id = Company.objects.get(user_id=id)
	cid = company_id.id
	result = Add_new_ad_type.objects.filter(company_id=cid)
	context = {'result' : result}
	return render(request, 'agency/all_ad_types.html', context)

def add_new_ad_type_delete(request, id):
	result = Add_new_ad_type.objects.get(pk=id)
	result.delete()
	return redirect('/agency/all_ad_types')

def add_new_ad_type_edit(request,id):
	result = Add_new_ad_type.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'agency/add_new_ad_type_edit.html', context)

def add_new_ad_type_update(request, id):
	img = request.FILES['image']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(img.name, img)
	
	data = {
				'size'   :request.POST['size'],
				'page_no'  :request.POST['page'],
				'description':request.POST['description'],
				'price':request.POST['price'],
				'mode':request.POST['mode'],
				'image_name' : img.name
			}
	Add_new_ad_type.objects.update_or_create(pk=id, defaults=data)
	return redirect('/agency/all_ad_types')

def orders(request):
	id = request.user.id
	query = Company.objects.get(user_id=id)
	cid = query.id

	result = Order.objects.filter(company_id=cid)
	context = {'result' : result}
	return render(request, 'agency/orders.html', context)	


