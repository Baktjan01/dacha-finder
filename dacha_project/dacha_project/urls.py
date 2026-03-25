from django.contrib import admin
from django.urls import path, include
from bot.views import webhook

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("finder_app.urls")),  # <-- теперь сработает
    path('webhook/', webhook),
]
