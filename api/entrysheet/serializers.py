from rest_framework import serializers
from api.entrysheet.models import EntrySheet

class EntrySheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrySheet
        fields = ['id', 'text', 'label']
