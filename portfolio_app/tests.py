from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpassword')
        self.user_profile = UserProfile.objects.create(
            user=self.user, home_address='123 Test Street', phone_number='1234567890')
    
    def test_profile_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Profile')
        self.assertContains(response, '123 Street')
        self.assertContains(response, '88546834765')
    
    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/edit_profile/', {'home_address': '456  Street', 'phone_number': '345353453'})
        self.assertEqual(response.status_code, 200)
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.home_address, '456Street')
        self.assertEqual(user_profile.phone_number, '9876543210')

