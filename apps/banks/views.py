from django.shortcuts import render, get_object_or_404
from .models import Bank

def bank_directory(request):
    banks = Bank.objects.all()
    return render(request, 'banks/bank_directory.html', {'banks': banks})

def bank_detail(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    return render(request, 'banks/bank_detail.html', {'bank': bank})