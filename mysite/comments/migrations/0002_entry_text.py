# Generated by Django 3.0.1 on 2020-02-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]