from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=('Currency')),
    path('detail', views.detail, name= 'detail'),
    path('search', views.search, name='search'),
]