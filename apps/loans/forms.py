from django import forms

class LoanApplicationForm(forms.Form):
    # Define fields for the loan application form
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Loan Amount")
    term = forms.IntegerField(label="Loan Term (in months)")
    purpose = forms.CharField(max_length=255, label="Purpose of Loan")
