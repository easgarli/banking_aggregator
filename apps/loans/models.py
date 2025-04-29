from django.db import models

class Loan(models.Model):
    LOAN_TYPE_CHOICES = [
        ('consumer', 'Consumer Loan'),
        ('mortgage', 'Mortgage'),
        ('car', 'Car Loan'),
        ('business', 'Business Loan'),
    ]

    bank = models.ForeignKey('banks.Bank', on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_term_months = models.IntegerField()
    total_repayment_amount = models.DecimalField(max_digits=15, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=15, decimal_places=2)
    fees = models.TextField(blank=True, null=True)
    required_documents = models.TextField(blank=True, null=True)
    special_offers = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.loan_type} - {self.amount} AZN"