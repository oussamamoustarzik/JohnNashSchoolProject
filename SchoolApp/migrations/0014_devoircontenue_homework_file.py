# Generated by Django 4.2.1 on 2023-06-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0013_devoir_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='devoircontenue',
            name='homework_file',
            field=models.FileField(blank=True, null=True, upload_to='homeworks/'),
        ),
    ]