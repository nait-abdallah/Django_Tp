from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('products/',views.products, name='products'),
    path('customers/<str:pk>/',views.customers, name='customers'),
    path('create_order/',views.createOrder,name='create_order'),
    path('update_order/<str:pk_up>/',views.createOrder,name='update_order'),
    path('creat_customer',views.creatCustomer,name='creat_customer'),
]
