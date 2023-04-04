# Generated by Django 4.1.5 on 2023-04-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0009_alter_createservice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createservice',
            name='image',
            field=models.ImageField(upload_to='img/service_provider'),
        ),
        migrations.AlterField(
            model_name='createservice',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='createservice',
            name='opening_and_closing_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='createservice',
            name='salon_color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='createservice',
            name='salon_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='createservice',
            name='salon_services',
            field=models.TextField(max_length=200),
        ),
    ]
