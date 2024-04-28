from django.urls import path
from authentication.views import register_pengguna,login_user,logout_user,register_label, registration_type
app_name = 'authentication'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/pengguna/', register_pengguna, name='register_pengguna'),
    path('register/label/', register_label, name='register_label'),
    path('register/', registration_type, name='register'),
]