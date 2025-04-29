from django.test import TestCase
from .models import Loan

class LoanModelTest(TestCase):

    def setUp(self):
        Loan.objects.create(
            loan_type='Consumer Loan',
            amount=10000,
            interest_rate=5.0,
            term=24,
            bank_name='Bank A'
        )

    def test_loan_creation(self):
        loan = Loan.objects.get(loan_type='Consumer Loan')
        self.assertEqual(loan.amount, 10000)
        self.assertEqual(loan.interest_rate, 5.0)
        self.assertEqual(loan.term, 24)
        self.assertEqual(loan.bank_name, 'Bank A')

class LoanViewTest(TestCase):

    def test_loan_comparison_view(self):
        response = self.client.get('/loans/compare/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loans/loan_comparison.html')