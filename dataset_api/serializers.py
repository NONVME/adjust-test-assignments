from rest_framework import serializers

from .models import Dataset


class DataSerializer(serializers.ModelSerializer):
    group_by = serializers.CharField(read_only=True)
    cpi = serializers.FloatField(read_only=True)

    class Meta:
        model = Dataset
        fields = [
            'date', 'channel', 'country', 'os', 'impressions', 'clicks',
            'installs', 'spend', 'revenue', 'group_by', 'cpi'
        ]
        read_only_fields = [
            'date', 'channel', 'country', 'os', 'impressions', 'clicks',
            'installs', 'spend', 'revenue'
        ]
