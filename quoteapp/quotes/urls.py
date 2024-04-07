from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='index_paginate'),
    path('tag/<int:tag_id>', views.tag_details, name='tag_details'),
    path('author/<int:author_id>', views.author_details, name='author_details'),
]
