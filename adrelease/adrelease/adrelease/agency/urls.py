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
from agency import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('add_new_ad_type', views.add_new_ad_type, name='add_new_ad_type'),
    path('add_new_ad_type_store', views.add_new_ad_type_store, name='add_new_ad_type_store'),
    path('add_new_ad_type_edit/<int:id>', views.add_new_ad_type_edit, name='add_new_ad_type_edit'),
    path('add_new_ad_type_update/<int:id>', views.add_new_ad_type_update, name='add_new_ad_type_update'),
    path('add_new_ad_type_delete/<int:id>', views.add_new_ad_type_delete, name='add_new_ad_type_delete'),
    path('all_ad_types', views.all_ad_types, name='all_ad_types'),
    path('orders', views.orders, name='orders'),
   
] 
