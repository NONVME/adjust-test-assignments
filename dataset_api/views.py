from rest_framework.viewsets import ModelViewSet

from .models import Dataset
from .serializers import DataSerializer


class DataViewSet(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DataSerializer
