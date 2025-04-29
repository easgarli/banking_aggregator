from django.urls import path
from . import views

urlpatterns = [
    path('', views.bank_directory, name='bank_directory'),
    path('<int:bank_id>/', views.bank_detail, name='bank_detail'),
]