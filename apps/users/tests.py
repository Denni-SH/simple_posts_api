from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User
from . import test_fixtures


class BaseUserTestCase(APITestCase):

    def setUp(self):
        super().setUpClass()
        self.client.post(
            reverse('register'), test_fixtures.DATA_SUPERADMIN_INPUT,
        )

    def fill_database_with_users(self):
        for user in test_fixtures.DATA_USERS:
            self.client.post(reverse('register'), user)


class CreateUserTestCase(BaseUserTestCase):

    def setUp(self):
        super().setUpClass()

    def test_correct_check_user_username(self):
        response = self.client.get(
            reverse(
                'check_username',
                kwargs=test_fixtures.DATA_CHECK_USERNAME_INPUT,
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, test_fixtures.DATA_CHECK_USERNAME_OUTPUT,
        )

    def test_correct_create_user(self):
        response = self.client.post(
            reverse('register'), test_fixtures.DATA_SUPERADMIN_INPUT,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_create_user_without_email(self):
        response = self.client.post(
            reverse('register'), test_fixtures.DATA_REGISTER_MISSED_EMAIL,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginUserTestCase(BaseUserTestCase):

    def test_correct_login_user(self):
        response = self.client.post(
            reverse('login'), test_fixtures.DATA_LOGIN_CORRECT,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTestCase(BaseUserTestCase):

    def setUp(self):
        super().setUp()
        self.fill_database_with_users()
        self.user = User.objects.get(id=2)
        self.client.force_login(user=self.user)

    def test_correct_get_user(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_fixtures.DATA_USER_OUTPUT)

    def test_correct_update_user(self):
        response = self.client.put(
            reverse('user'),
            data=test_fixtures.DATA_UPDATE_INPUT,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_fixtures.DATA_UPDATE_OUTPUT)

    def test_correct_delete_user(self):
        response = self.client.delete(
            reverse('user'),
            data=test_fixtures.DATA_UPDATE_INPUT,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
