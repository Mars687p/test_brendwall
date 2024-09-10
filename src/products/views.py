from typing import Any

from django.views.generic import ListView
from rest_framework import viewsets

from .forms import AddProductPform
from .models import Products
from .serializers import CreateProductSerializer, GetProductsSerializer


class ProductsViews(ListView):
    model = Products
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = AddProductPform()
        return context


class CRUDCityViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = CreateProductSerializer
    http_method_names = ['post', 'delete', 'put']


class GetCityViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = GetProductsSerializer
    http_method_names = ['get']
