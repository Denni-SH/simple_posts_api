from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {
            'username': 'mike', 'email': 'Mike@gmail.com',
            'last_name': 'Tyson', 'password':'1234'
        }

    def test_can_create_user(self):
        response = self.client.post(reverse('register'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
