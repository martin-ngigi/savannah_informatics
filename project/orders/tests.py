from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Order
from django.urls import reverse
import json
import uuid
import random
import string

class OrderAPITestCase(APITestCase):
    def test_get_orders(self):
        url = '/orders/all/'
        response = self.client.get(url)

        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

'''
    def test_create_order(self):
        url = '/orders/all/'

        # Sample JSON data for the request
        data = {
            # "code": ''.join(random.choices(string.ascii_uppercase, k=8)),
            "quantity" : "3",
            "user": 1,
            "items": [
                "d713bcd4-f2e6-41c8-bc27-bc7e8ead44f4",
                "c84beb74-76c9-4429-86f1-896c8d822ec5"
            ],
            "amount": 200
        }

        # Convert data to JSON
        json_data = json.dumps(data)

        # Make the POST request with application/json Content-Type
        response = self.client.post(url, json_data, content_type='application/json')

        # Assert the response status code is 201
        self.assertEqual(response.status_code, 201)

        # Assert the response Order count is 1
        self.assertEqual(Order.objects.count(), 1)

        # Assert the Content-Type header is present
        self.assertIn('Content-Type', response)

        # Assert the Content-Type is 'application/json'
        self.assertEqual(response['Content-Type'], 'application/json')


        # Assert the response data matches the expected structure
        # expected_data = {
        #     "id": response.data['id'],
        #     "code": response.data['code'],
        #     "amount": response.data['amount'],
        #     "quantity": response.data['quantity'],
        #     "created_at": response.data['created_at'],
        #     "updated_at": response.data['updated_at'],
        #     "user": response.data['user'],
        #     "items": response.data['items']
        # }

        expected_data = {
            "id": response.data['id'],
            "code": response.data['code'],
            "amount": 200,
            "quantity": "3",
            "created_at": response.data['created_at'],
            "updated_at": response.data['updated_at'],
            "user": 1,
            "items": [
                "c84beb74-76c9-4429-86f1-896c8d822ec5",
                "d713bcd4-f2e6-41c8-bc27-bc7e8ead44f4"
            ]
        }

        self.assertEqual(response.data, expected_data)
'''