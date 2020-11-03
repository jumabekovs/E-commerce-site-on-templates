from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create/', views.createOrder, name='create_order'),
    path('update/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete/<str:pk>', views.deleteOrder, name='delete_order'),
]