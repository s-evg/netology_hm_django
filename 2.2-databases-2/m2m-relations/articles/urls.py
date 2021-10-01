from django.urls import path

from articles.views import *

urlpatterns = [
    path('', articles_list_view, name='articles'),
    path('post/<slug:slug>', post_view, name='post'),
]
