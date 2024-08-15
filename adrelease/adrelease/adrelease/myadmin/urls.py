"""adrelease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('', views.register, name='register'),
    path('add_state', views.add_state, name='add_state'),
    path('state_store', views.state_store, name='state_store'),
    path('all_states', views.all_states, name='all_states'),
    path('add_city', views.add_city, name='add_city'),
    path('city_store', views.city_store, name='city_store'),
    path('view_location', views.view_location, name='view_location'),
    path('view_city/<int:id>', views.view_city, name='view_city'),
    path('add_agency', views.add_agency, name='add_agency'),
    path('add_agency_store', views.add_agency_store, name='add_agency_store'),
    path('msg', views.msg, name='msg'),
    path('agency', views.agency, name='agency'),
    path('view_agency/<int:id>', views.view_agency, name='view_agency'),
    path('customers', views.customers, name='customers'),
    path('view_customers/<int:id>', views.view_customers, name='view_customers'),
    path('orders', views.orders, name='orders'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('feedback', views.feedback, name='feedback'),
    path('form', views.form, name='form'),
    path('table', views.table, name='table'),
]
