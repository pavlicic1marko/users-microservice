from django.urls import path
from . import views


urlpatterns = [
    path('todo/test', views.getRoutes, name='routes'),
    path('todo/products', views.getProducts, name='products'),
    path('todo/products/<str:pk>', views.getProductsById, name='products'),



]