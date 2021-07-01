from django.shortcuts import render
from .models import Product

def home(request):
	products_list = Product.objects.all()
	return render(request, 'shop/home.html', {'products_list': products_list})
