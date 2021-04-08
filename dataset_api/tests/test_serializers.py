from django.test import TestCase

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


class DataSerializerTestCase(TestCase):
    def test_data_serialize(self):
        adv_campaign = Dataset.objects.create(**data_adv_compaign)
        serializer_data = DataSerializer(adv_campaign).data
        expected_data = {
            'id': adv_campaign.id,
            'date': '2017-05-17',
            'channel': 'adcolony',
            'country': 'US',
            'os': 'android',
            'impressions': 19887,
            'clicks': 494,
            'installs': 76,
            'spend': '148.20',
            'revenue': '149.04',
        }
        self.assertEqual(serializer_data, expected_data)
