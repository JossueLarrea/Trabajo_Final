# Generated by Django 3.1.7 on 2021-02-25 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
