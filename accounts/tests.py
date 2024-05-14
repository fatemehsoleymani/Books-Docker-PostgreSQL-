from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            password='test123',
            email='test@yahoo.com'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='sami',
            password='sami123',
            email='sami@yahoo.com',
        )
        self.assertEqual(user.username, 'sami')
        self.assertEqual(user.email, 'sami@yahoo.com')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)