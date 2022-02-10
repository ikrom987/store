from django.urls import path
from . import views

urlpatterns = [
    # Index urls
    path("", views.control_index, name="control_index"),

    # Category urls
    path("category/add/", views.category_add, name="category_add"),
    path("category/all/", views.category_all, name="category_all"),
    path("category/detail/<str:slug>/", views.category_detail, name="category_detail"),
        path("category/create/", views.category_create, name="category_create"),
        path("category/edit/", views.category_edit, name="category_edit"),
        path("category/delete/", views.category_delete, name="category_delete"),


    # Product urls
    path("product/add/", views.product_add, name="product_add"),
    path("product/all/", views.product_all, name="product_all"),
    path("product/detail/<str:slug>/", views.product_detail, name="product_detail"),
        path("product/create/", views.product_create, name="product_create"),
        path("product/edit/", views.product_edit, name="product_edit"),
        path("product/delete/", views.product_delete, name="product_delete"),

]