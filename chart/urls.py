from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart_list, name='chart_list'),
    path('<str:chart_type>/', views.chart_detail, name='chart_detail'),
]