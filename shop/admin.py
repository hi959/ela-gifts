from django.contrib import admin


from .models import Product, Categorie, HeaderImages
# Register your models here.


admin.site.register(Product)
admin.site.register(Categorie)
admin.site.register(HeaderImages)
