from django.urls import path 
from .import views

urlpatterns=[
    path('',views.account,name='account'),
    path('cart',views.cart,name='cart')
]