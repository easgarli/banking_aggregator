from django.test import TestCase
from .models import Bank

class BankModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Bank.objects.create(name="Test Bank", logo="test_logo.png")

    def test_bank_name(self):
        bank = Bank.objects.get(id=1)
        self.assertEqual(bank.name, "Test Bank")

    def test_bank_logo(self):
        bank = Bank.objects.get(id=1)
        self.assertEqual(bank.logo, "test_logo.png")