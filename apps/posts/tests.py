import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User
from . import test_fixtures


class BasePostTestCase(APITestCase):

    def setUp(self):
        super().setUpClass()
        self.client.post(
            reverse('register'), test_fixtures.DATA_SUPERADMIN_INPUT,
        )
        self.user = User.objects.get(id=1)
        self.client.force_login(user=self.user)

    def fill_database_with_posts(self):
        for post in test_fixtures.DATA_POSTS:
            self.client.post(
                reverse('create_post'),
                json.dumps(post),
                content_type="application/json",
            )


class CreatePostTestCase(BasePostTestCase):

    def setUp(self):
        super().setUp()
        
    def test_correct_create_post(self):
        response = self.client.post(
            reverse('create_post'),
            json.dumps(test_fixtures.DATA_POST_INPUT),
            content_type="application/json",
        )
        del response.data['timestamp']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, test_fixtures.DATA_POST_OUTPUT)

    def test_wrong_create_post_without_title(self):
        response = self.client.post(
            reverse('register'),
            json.dumps(test_fixtures.DATA_POST_WITHOUT_TITLE),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PostTestCase(BasePostTestCase):

    def setUp(self):
        super().setUp()
        self.fill_database_with_posts()
        self.client.force_login(user=self.user)

    def test_correct_get_post(self):
        response = self.client.get(
            reverse('post', kwargs=test_fixtures.DATA_POST_GET_INPUT),
        )
        del response.data['timestamp']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_fixtures.DATA_POST_GET_OUTPUT)

    def test_correct_update_user(self):
        response = self.client.put(
            reverse('post', kwargs=test_fixtures.DATA_POST_GET_INPUT),
            data=test_fixtures.DATA_POST_UPDATE_INPUT,
        )
        del response.data['timestamp']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_fixtures.DATA_POST_UPDATE_OUTPUT)

    def test_correct_delete_user(self):
        response = self.client.delete(
            reverse('post', kwargs=test_fixtures.DATA_POST_GET_INPUT),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostListTestCase(BasePostTestCase):

    def setUp(self):
        super().setUp()
        self.fill_database_with_posts()
        self.client.force_login(user=self.user)

    def test_correct_get_post_list(self):
        response = self.client.get(
            reverse('get_posts_list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = dict(response.data)
        for post in results['results']:
            del post['timestamp']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results, test_fixtures.DATA_POST_LIST)
