from rest_framework import serializers
from .models import EntrySheet

class EntrySheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySheet
        fields = ['id', 'text', 'label']
