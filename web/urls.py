from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.web_index, name="web_index"),
    path("category/<int:id>/", views.web_category, name="web_category"),
    path("product/<str:slug>", views.web_detail, name="web_detail"),
    path("cart/", views.web_cart, name="web_cart"),
    path("checkout/", views.web_checkout, name="web_checkout"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
        path("signin/", views.sign_in, name="sign_in"),
        path("signup/", views.sign_up, name="sign_up"),
        path("logout/", views.log_out, name="log_out"),

    # Add to cart
    path("add/", views.add_to_cart, name="add_to_cart"),
    path("remove/", views.remove_order_item, name="remove_order_item"),
    path("plus/", views.item_plus, name="item_plus"),
    path("minus/", views.item_minus, name="item_minus"),
    path("complete/", views.complete, name="complete"),

    # RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="web/login/reset.html"), name="password_reset"),
    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name="web/login/reset_done.html"), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="web/login/reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name="web/login/reset_complete.html"), name="password_reset_complete"),



]