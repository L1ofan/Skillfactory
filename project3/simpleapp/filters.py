from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):

   class Meta:
       model = Product
       fields = {
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',
               'gt',
           ],
       }