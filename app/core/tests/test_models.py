from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test_create_user_with_email_successful"""
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normailzed(self):
        """test email normalized"""
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test invalid email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testqwe123')

    def test_new_user_as_superuser(self):
        """check if the user is superuser"""
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
