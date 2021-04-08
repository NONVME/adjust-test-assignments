from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from dataset_api.models import Dataset
from dataset_api.serializers import DataSerializer

data_adv_compaign = {
    'date': '2017-05-17',
    'channel': 'adcolony',
    'country': 'US',
    'os': 'android',
    'impressions': 19887,
    'clicks': 494,
    'installs': 76,
    'spend': 148.2,
    'revenue': 149.04,
}


class DataApiTestCase(APITestCase):
    def test_get(self):
        adv_campaign = Dataset.objects.create(**data_adv_compaign)
        url = reverse('dataset-detail', args=(1,))
        response = self.client.get(url)
        serializer_data = DataSerializer(adv_campaign).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
