from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]