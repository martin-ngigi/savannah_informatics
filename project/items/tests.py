from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Item
import json
import uuid
import random
import string

class OrderAPITestCase(APITestCase):
    def test_get_item(self):
        url = '/items/all/'
        response = self.client.get(url)

        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)
    
    def test_create_item(self):
        url = '/items/all/'

        # Sample JSON data for the request
        data = {
            "name": "Sugar",
            "quantity": "2 Kg",
            "price": 400,
            "description": "Mumias sugar 2 Kg"
        }

        # Convert data to JSON
        json_data = json.dumps(data)

        # Make the POST request with application/json Content-Type
        response = self.client.post(url, json_data, content_type='application/json')

        # Assert the response Item count is 1
        self.assertEqual(Item.objects.count(), 1)

        # Assert the response status code is 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert the Content-Type header is present
        self.assertIn('Content-Type', response)

        # Assert the Content-Type is 'application/json'
        self.assertEqual(response['Content-Type'], 'application/json')


        # Assert the response data matches the expected structure
        # expected_data = {
        #     "id": response.data['id'],
        #     "name": response.data['name'],
        #     "quantity": response.data['quantity'],
        #     "price": response.data['price'],
        #     "description": response.data['description']
        # }
    
        # self.assertEqual(response.data, expected_data)
