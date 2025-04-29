from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan
from .forms import LoanApplicationForm

def loan_comparison(request):
    loans = Loan.objects.all()  # Fetch all loan products
    context = {
        'loans': loans,
    }
    return render(request, 'loans/loan_comparison.html', context)

def apply_loan(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            # Process the application (e.g., save to database, send to bank, etc.)
            # Redirect to a success page or display a success message
            return redirect('loan_success')  # Replace with your success URL
    else:
        form = LoanApplicationForm()
    
    context = {
        'loan': loan,
        'form': form,
    }
    return render(request, 'loans/apply_loan.html', context)

def loan_details(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    return render(request, 'loans/loan_details.html', {'loan': loan})

def home(request):
    print("DEBUG: Home view called")  # Debugging statement
    try:
        response = render(request, 'home.html')
        print("DEBUG: Template rendered successfully")  # Debugging statement
        return response
    except Exception as e:
        print(f"DEBUG: Error rendering template - {e}")  # Debugging statement
        raise