from django.urls import path

from .views import CRUDCityViewSet, GetCityViewSet, ProductsViews

urlpatterns = [
    path('', ProductsViews.as_view()),
    path('api/v1/products/',
         GetCityViewSet.as_view({'get': 'list'}), name='list'),
    path('api/v1/products/create/',
         CRUDCityViewSet.as_view({'post': 'create'})),
]
