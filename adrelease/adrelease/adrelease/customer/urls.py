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
from django.urls import path,include,re_path
from customer import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('rstore', views.rstore, name='rstore'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),  
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('inquiry_store', views.inquiry_store, name='inquiry_store'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('post_ad', views.post_ad, name='post_ad'),
    path('select_img', views.select_img, name='select_img'),
    path('selected_ad_types', views.selected_ad_types, name='selected_ad_types'),
    path('order/<int:id>', views.order, name='order'),
    path('order_store/<int:id>', views.order_store, name='order_store'),
    path('booking', views.booking, name='booking'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('success', views.success, name='success'),
    re_path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
]
