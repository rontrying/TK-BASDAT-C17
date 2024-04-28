from django.urls import path
from .views import *
app_name = 'royalti'

urlpatterns = [
    path('', list_royalti, name='list_royalti'),
    # Tambahkan pola URL lain sesuai kebutuhan Anda
]