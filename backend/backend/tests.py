from django.contrib.auth.models import User
from django.test import TestCase


class TestDatabase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testUser',
            email='user@foo.com',
            password='password',
        )
        user.save()
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
