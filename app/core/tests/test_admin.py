"""
Test for Django Admin modification
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import client


class adminSiteTest(TestCase):
    """django admin modification tests"""
    def setUp(self):
        self.client = client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            passworld='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user - get_user_model().objects.create_user(
            email='user@example.com',
            passworld='testpass123',
            name='Test User',
        )
    def test_user_list(self):
        """Test that users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
