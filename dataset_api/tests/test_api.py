from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dataset_api.models import Dataset
from dataset_api.serializers import DataSerializer
from dataset_api.utils import disk_import

DATASET_FROM_DISK = {'path': 'dataset_api/tests/fixtures/dataset_list.csv',
                     'quantity_row': 1096}
DATASET_ONE_COMPAIGN = {
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


class OneCompaignApiTestCase(APITestCase):
    def test_get(self):
        one_campaign = Dataset.objects.create(**DATASET_ONE_COMPAIGN)
        url = reverse('dataset-list')
        response = self.client.get(url)
        expected_data = DataSerializer(one_campaign).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, *response.data)


class DataSetApiTestCase(APITestCase):
    def setUp(self):
        disk_import(DATASET_FROM_DISK['path'])
        self.url = reverse('dataset-list')

    def test_import_data(self):
        imported_quantity = len(list(Dataset.objects.all()))
        exepcted_quantity = DATASET_FROM_DISK['quantity_row']
        self.assertEqual(imported_quantity, exepcted_quantity)

    def test_first_api_case(self):
        response = self.client.get(self.url
                                   + """?date__lte=2017-06-01&group_by=country\
&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 25)

    def test_second_api_case(self):
        response = self.client.get(self.url
                                   + """?date__range=2017-05-01,2017-05-31\
&ordering=date&os=ios&group_by=date&limit=installs""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 15)

    def test_third_api_case(self):
        response = self.client.get(self.url
                                   + """?date__lte=2017-06-01&country=US\
&group_by=os&ordering=-revenue&limit=revenue""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 2)

    def test_fourth_api_case(self):
        response = self.client.get(self.url
                                   + """?country=CA&group_by=channel&cpi=cpi&\
limit=spend&ordering=-cpi""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 4)
