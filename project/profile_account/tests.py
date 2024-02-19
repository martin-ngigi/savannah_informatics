from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status

class OrderAPITestCase(APITestCase):

    def test_get_users(self):
        url = '/users/all/'
        response = self.client.get(url)

        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)