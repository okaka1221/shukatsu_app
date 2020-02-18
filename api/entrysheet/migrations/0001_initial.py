# Generated by Django 3.0 on 2020-02-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntrySheetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('keywords', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('text', models.TextField(unique=True)),
                ('label', models.BooleanField(verbose_name='')),
            ],
        ),
    ]
