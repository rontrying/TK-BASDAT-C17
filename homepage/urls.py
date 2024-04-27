from django.urls import path
from homepage.views import *
urlpatterns = [
    path('', homepage_view, name='homepage'),
]