from django.db import models

class EntrySheet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField(unique=True)
    label = models.BooleanField(verbose_name='', blank=False, null=False)