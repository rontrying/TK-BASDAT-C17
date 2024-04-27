from django.urls import path
from authentication.views import register,login_user,logout_user
app_name = 'authentication'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
]