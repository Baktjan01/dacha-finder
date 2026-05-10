from django.urls import path
from . import views

urlpatterns = [
    path('dachas/', views.DachaListView.as_view(), name='dacha-list'),
    path('dachas/<int:pk>/', views.DachaDetailView.as_view(), name='dacha-detail'),
    path('dachas/<int:pk>/availability/', views.CheckAvailabilityView.as_view(), name='dacha-availability'),
    path('bookings/', views.CreateBookingView.as_view(), name='create-booking'),
]
