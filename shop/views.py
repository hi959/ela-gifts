from django.shortcuts import render, redirect


from .models import Product, Categorie, HeaderImages

def home(request):
	header_images = HeaderImages.objects.all()
	hot_products = Product.objects.filter(hot_product=True)
	recomanded_products = Product.objects.filter(recomanded_product=True)
	products_list = Product.objects.all()
	categories = Categorie.objects.all()
	return render(request, 'shop/home.html', {'hot_products': hot_products, 'recomanded_products': recomanded_products, 'categories': categories, 'header_images':header_images })


def show_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'shop/product.html', {'product': product})


def category(request, category_id):
	try:
		products = Product.objects.filter(category=category_id)
		category_name = Categorie.objects.get(pk=category_id)
		return render(request, 'shop/category.html', {'products': products, 'category':category_name})
	except:
		category = Categorie.objects.get(name=category_id)
		products = Product.objects.filter(category=category.id)

		return render(request, 'shop/category.html', {'products': products, 'category':category})


def search(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		if searched == " " or searched =="" or searched == "/":
			return redirect('home')
		else:
			categories = Categorie.objects.filter(name__contains=searched)
			products = Product.objects.filter(name__contains=searched)
			return render(request, 'shop/search.html',
			{'searched':searched, 'categories':categories, 'products':products})
	else:
		return render(request, 'shop/home.html')
