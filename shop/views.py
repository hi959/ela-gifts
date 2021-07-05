from django.shortcuts import render
from .models import Product

def home(request):
	hot_products = Product.objects.filter(hot_product=True)
	products_list = Product.objects.all()
	return render(request, 'shop/home.html', {'hot_products': hot_products})
