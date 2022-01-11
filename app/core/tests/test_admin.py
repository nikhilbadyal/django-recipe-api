from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="nikhil@nikhil.com",
            password="nikhil"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email="aikhil@aikhil.com", password='aikhil', name='Test User')

    def test_for_user_listed(self):
        """Test that user are listed"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Create User page works"""
        url = reverse('admin:core_user_add', )
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
