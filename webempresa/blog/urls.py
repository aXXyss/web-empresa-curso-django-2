from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>', views.category, name='category'),    #  <int:category_id> el INT convierte en Integer la cadena de exto
]