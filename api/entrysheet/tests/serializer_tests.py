from django.test import TestCase
from api.entrysheet.serializers import EntrySheetSerializer
from api.entrysheet.models import EntrySheet

class EntrySheetSerializerTest(TestCase):
    def setUp(self):
        self.entrysheet_attribute = {
            'text': '私の強みはリーダーシップです。',
            'label': True
        }

        self.entrysheet_data = {
            'text': '私の強みは、人を巻き込む力です。',
            'label': False
        }

        self.entrysheet = EntrySheet.objects.create(**self.entrysheet_attribute)
        self.serializer = EntrySheetSerializer(instance=self.entrysheet)

    def test_contains_expected_field(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'text', 'label']))

    def test_unique_text_field(self):
        data = self.entrysheet_data
        data['text'] = '私の強みはリーダーシップです。'

        serializer = EntrySheetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_null_label_field(self):
        data = self.entrysheet_data
        data['label'] = None

        serializer = EntrySheetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_blunk_label_field(self):
        data = { 'text': self.entrysheet_data['text'] }

        serializer = EntrySheetSerializer(data=data)
        self.assertFalse(serializer.is_valid())