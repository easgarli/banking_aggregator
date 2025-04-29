from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_comparison, name='loan_comparison'),
    path('apply/<int:loan_id>/', views.apply_loan, name='apply_loan'),
    path('details/<int:loan_id>/', views.loan_details, name='loan_details'),
]