from rest_framework import serializers
from .models import EntrySheetModel

class EntrySheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySheetModel
        fields = ['id', 'keywords', 'text', 'label']
