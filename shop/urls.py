from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<product_id>', views.show_product, name="show-product"),
    path('category/<category_id>', views.category, name="category")
]
