from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Create your views here.

@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form':form
    }
    return render(request, 'dashboard/product.html', context)

def delete_product(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)

def update_product(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def order(request):
    return render(request, 'dashboard/order.html')