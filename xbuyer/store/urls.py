from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('shop/', views.shop, name='shop'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  # Register page
]
