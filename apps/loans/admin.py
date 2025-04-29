from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount']  # Removed 'name' if it doesn't exist in the Loan model
    search_fields = ('bank__name', 'loan_type')
    list_filter = ('loan_type', 'bank')
    ordering = ['id']