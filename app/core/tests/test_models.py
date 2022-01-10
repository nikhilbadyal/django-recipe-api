from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with email and password"""
        email = "nikhil@nikhil.com"
        password = "nikhil"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """Test the email for a new user in normalized"""
        email = "nikhil@NIKHIL.COM"
        user = get_user_model().objects.create_user(email, '12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Email is a must field"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_super_user(self):
        """Test creating of superuser"""
        user = get_user_model().objects.create_superuser('nikhil@nikhil.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
