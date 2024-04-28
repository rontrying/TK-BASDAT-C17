from django.urls import path
from .views import user_dashboard

urlpatterns = [
    path('', user_dashboard, name='dashboard'),
]
