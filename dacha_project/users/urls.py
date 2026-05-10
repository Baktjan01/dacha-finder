from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.telegram_auth, name='telegram-auth'),
]
