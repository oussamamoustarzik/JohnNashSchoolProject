# Generated by Django 4.2.1 on 2023-07-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0021_alter_cours_id_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='nbr_eleve_classe',
            field=models.PositiveIntegerField(default=30),
        ),
    ]
