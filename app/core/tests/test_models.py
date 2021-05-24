from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test creating a new user with an email and password"""
    email = 'njirucharles@gmail.com'
    password = 'testpassw123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    self.assertEqual(user.email,email)
    self.assertTrue(user.check_password(password))