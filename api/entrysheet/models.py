from django.db import models

class EntrySheetModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    keywords = models.CharField(max_length=100, blank=True, null=True, default='')
    text = models.TextField(unique=True)
    label = models.BooleanField(verbose_name='', blank=False, null=False)