from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    totale_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'totale_orders':totale_orders,'delivered':delivered,'pending':pending}

    return render(request , 'accounts/dashboard.html' ,context)

def products(request):
    products = Product.objects.all()

    return render(request , 'accounts/products.html',{'products' : products})

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = { 'customer':customer ,'orders':orders ,'orders_count':orders_count}
    return render(request , 'accounts/customers.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)

def creatCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/customer_form.html',context)

def updateOrder(request,pk_up):
    form = OrderForm()
    context={'form':form}
    return render(request,'accounts/order_form.html',context)
