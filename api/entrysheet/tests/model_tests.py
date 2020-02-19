from django.test import TransactionTestCase
from api.entrysheet.models import EntrySheet
from api.entrysheet.serializers import EntrySheetSerializer

class EntrySheetModelTest(TransactionTestCase):
    def setUp(self):
        EntrySheet.objects.create(text='私の強みはリーダーシップです。', label=True)
        
    def test_save_new_data(self):
        prev_count = EntrySheet.objects.all().count()

        try:
            EntrySheet.objects.create(text='私はコツコツと努力ができる人間です', label=False)
        except:
            pass
        
        self.assertEqual(EntrySheet.objects.all().count(), prev_count+1)

    def test_invalid_unique_text_field(self):
        prev_count = EntrySheet.objects.all().count()

        try:
            EntrySheet.objects.create(text='私の強みはリーダーシップです。', label=False)
        except:
            pass
        
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)

    def test_invalid_null_label_field(self):
        prev_count = EntrySheet.objects.all().count()

        try:
            EntrySheet.objects.create(text='私はコツコツと努力ができる人間です', label=None)
        except:
            pass
        
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)

    def test_invalid_blunk_label_field(self):
        prev_count = EntrySheet.objects.all().count()

        try:
            EntrySheet.objects.create(text='私はコツコツと努力ができる人間です')
        except:
            pass
        
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)