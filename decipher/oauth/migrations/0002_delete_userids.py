# Generated by Django 5.0.6 on 2024-06-05 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserIds',
        ),
    ]