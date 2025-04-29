from django.test import TestCase
from .models import User  # Assuming you have a User model defined in models.py

class UserModelTests(TestCase):

    def setUp(self):
        # Create a user instance for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

    def test_user_creation(self):
        """Test that a user can be created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_email(self):
        """Test that the user's email is set correctly."""
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_str(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), 'testuser')  # Assuming __str__ method returns username

    def tearDown(self):
        # Clean up after tests
        self.user.delete()