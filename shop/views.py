from django.shortcuts import render
from .models import Product, Categorie

def home(request):
	hot_products = Product.objects.filter(hot_product=True)
	recomanded_products = Product.objects.filter(recomanded_product=True)
	products_list = Product.objects.all()
	categories = Categorie.objects.all()
	return render(request, 'shop/home.html', {'hot_products': hot_products, 'recomanded_products': recomanded_products, 'categories': categories})


def show_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'shop/product.html', {'product': product})


def category(request, category_id):
	products = Product.objects.filter(category=category_id)
	return render(request, 'shop/category.html', {'products': products})
