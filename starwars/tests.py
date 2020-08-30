from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from starwars.models import Planet, People
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from starwars import views


class PlanetTests(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PlanetModelViewSet.as_view({'get': 'list'})
        self.uri = '/planet/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.login(username="test", password="test")

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )
    
    def test_list(self):
        autorization = 'Token {}'.format(self.token.key)
        request = self.factory.get(self.uri,
            HTTP_AUTHORIZATION=autorization)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        url = reverse('planet-list')
        data = {
            'name': 'Tatooine',
            'population': '200000',
            'known_residents_count': 9
        }
        response = self.client.post(self.uri, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Planet.objects.count(), 1)
        self.assertEqual(Planet.objects.get().name, 'Tatooine')

    def test_retrieve(self):
        self.test_create()
        url =  reverse('planet-detail', args={1})
        url =  '/planet/12/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   
