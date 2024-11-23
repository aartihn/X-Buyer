from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('shop/', views.shop, name='shop'),  # Add Shop page URL
    path('login/', views.login, name='login'),  # Add Login page URL
]
