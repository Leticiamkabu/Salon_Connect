# Generated by Django 4.1.5 on 2023-01-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('salon_name', models.CharField(max_length=200)),
                ('salon_services', models.TextField(max_length=200)),
                ('opening_and_closing_time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]