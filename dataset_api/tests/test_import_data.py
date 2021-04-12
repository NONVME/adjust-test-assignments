from rest_framework.test import APITestCase

from dataset_api.models import Dataset
from dataset_api.utils import http_import

DATASET_FORM_URL_S = {'path': """https://gist.githubusercontent.com/NONVME/\
2d515e43ba23c59744b17db117824bbc/raw/7c4b7cc8a239acaf0bc1a576b6c1a17396104a52/\
gistfile1.csv""", 'quantity_row': 2}


class HttpDataImporterTestCase(APITestCase):
    def setUp(self):
        http_import(DATASET_FORM_URL_S['path'])

    def test_import_data(self):
        imported_quantity = len(list(Dataset.objects.all()))
        exepted_quantity = DATASET_FORM_URL_S['quantity_row']
        self.assertEqual(imported_quantity, exepted_quantity)
