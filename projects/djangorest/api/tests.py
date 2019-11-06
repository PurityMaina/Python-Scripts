from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """define the test suite for the bucketlist model here."""

    def setUp(self):
       """define the test client and other test variables here."""
       self.bucketlist_name = "crack all hackerank tests"
       self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
       """test the bucket model can create a bucketlist."""
       old_count = Bucketlist.objects.count()
       self.bucketlist.save()
       new_count = Bucketlist.objects.count()
       self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """" test suite for the api views."""
    def setUp(self):
        """" Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Earthdance'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """" Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code_status.HTTP_201_CREATED)