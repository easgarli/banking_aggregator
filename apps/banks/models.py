from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='bank_logos/', blank=True, null=True)  # Ensure Pillow is installed
    website = models.URLField()

    def __str__(self):
        return self.name

class LoanProduct(models.Model):
    bank = models.ForeignKey(Bank, related_name='loan_products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=50)  # e.g., Consumer Loan, Mortgage, etc.
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 5.00
    max_loan_amount = models.DecimalField(max_digits=15, decimal_places=2)  # e.g., 100000.00
    loan_term_months = models.IntegerField()  # e.g., 12, 24, 36, etc.
    fees = models.TextField(blank=True)  # Any associated fees
    special_offers = models.TextField(blank=True)  # Any special offers or promotions

    def __str__(self):
        return f"{self.product_name} - {self.bank.name}"