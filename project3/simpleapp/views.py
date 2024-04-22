from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'