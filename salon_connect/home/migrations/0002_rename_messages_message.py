# Generated by Django 4.1.5 on 2023-01-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
