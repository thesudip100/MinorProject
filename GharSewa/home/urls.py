from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer_register/', views.customer_register, name='customer_register'),
    path('prof_register/', views.prof_register, name='prof_register'),
    path('login/', views.loginPage, name='loginPage'),
    ]