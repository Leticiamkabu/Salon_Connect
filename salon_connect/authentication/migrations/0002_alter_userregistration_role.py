# Generated by Django 4.1.5 on 2023-04-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='role',
            field=models.CharField(choices=[('U', 'User'), ('S', 'Service Provider')], default='user', max_length=20),
        ),
    ]
