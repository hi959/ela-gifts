from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<product_id>', views.show_product, name="show-product"),
    path('product/<subimagenum>/<product_id>/', views.subimage, name="subimage"),
    path('category/<category_id>', views.category, name="category"),
    path('search', views.search, name="search"),
]
