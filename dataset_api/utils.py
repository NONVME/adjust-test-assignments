import csv
from typing import Iterable, Optional

import requests
from rest_framework import status

from dataset_api.models import Dataset

TIMEOUT = 15


def disk_import(path: str) -> None:
    with open(path) as csvfile:
        upload_csv_to_db(csvfile)


def http_import(url: str) -> Optional[int]:
    try:
        response = requests.get(url, timeout=TIMEOUT)
    except requests.exceptions.ReadTimeout:
        message = status.HTTP_408_REQUEST_TIMEOUT
    else:
        if response.ok:
            upload_csv_to_db(response.text.splitlines())
            message = status.HTTP_200_OK
            return message
        else:
            message = status.HTTP_400_BAD_REQUEST
            return message


def upload_csv_to_db(data: Iterable) -> None:
    reader = csv.reader(data)
    next(reader, None)
    for row in reader:
        Dataset.objects.get_or_create(
            date=row[0],
            channel=row[1],
            country=row[2],
            os=row[3],
            impressions=row[4],
            clicks=row[5],
            installs=row[6],
            spend=row[7],
            revenue=row[8],
        )
