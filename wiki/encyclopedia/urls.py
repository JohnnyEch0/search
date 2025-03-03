from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new_page", views.create_new_page, name="new_page"),
    path("random_page", views.random, name="random_page"),
    path("edit/<str:title>", views.edit, name="edit"),
    
]
