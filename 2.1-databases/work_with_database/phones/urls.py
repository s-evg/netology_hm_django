from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view),
    path('catalog/', show_catalog_view, name='catalog'),
    path('catalog/<slug:slug>/', show_product_view, name='phone'),
]
