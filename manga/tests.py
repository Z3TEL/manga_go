from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from manga.models import Manga

User = get_user_model()


class TestManga(TestCase):
    def setUp(self)-> None:
        self.user = User.objects.create_user('test32@mail.com',
                                             '1234',
                                             name='User1',
                                             is_active=True)
        self.admin = User.objects.create_superuser('admin@gmail.com',
                                                   '1234',
                                                   name='Admin1')
        self.user_token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)
        self.manga1 = Manga.objects.create(title='Test1',
                                           description='test1_desc',
                                           author='test1',
                                           artist='test1',
                                           genre='Horror')
        self.manga2 = Manga.objects.create(title='Test2',
                                           description='test2_desc',
                                           author='test2',
                                           artist='test2',
                                           genre='Seinen')
        self.manga1 = Manga.objects.create(title='Test3',
                                           description='test3_desc',
                                           author='test3',
                                           artist='test3',
                                           genre='Comedy')
        self.manga_payload = {
            'title': 'Test',
            'description': 'test_desc',
            'author': 'test1',
            'artist': 'test1',
            'genre ': 'Horror'
        }

    def test_list(self):
        client = APIClient()
        url = reverse('manga-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)

    def test_create_manga_as_anonymous_user(self):
        client = APIClient()
        url = reverse('manga-list')
        response = client.post(url, data=self.manga_payload)
        self.assertEqual(response.status_code, 401)

    def test_create_manga_as_regular_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=self.manga_payload)
        self.assertEqual(response.status_code, 403)

    def test_create_manga_as_admin_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=self.manga_payload)
        self.assertEqual(response.status_code, 201)

    def test_create_manga_without_title(self):
        data = self.manga_payload.copy()
        data.pop('title')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('title', response.data)

    def test_create_manga_without_description(self):
        data = self.manga_payload.copy()
        data.pop('description')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('description', response.data)

    def test_create_manga_without_author(self):
        data = self.manga_payload.copy()
        data.pop('author')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('author', response.data)

    def test_create_manga_without_artist(self):
        data = self.manga_payload.copy()
        data.pop('artist')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('manga-list')
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('artist', response.data)

