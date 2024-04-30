from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail, Create_product


urlpatterns = [

   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('create/', Create_product, name='product_create'),
]