# Generated by Django 4.2.1 on 2023-06-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0006_alter_devoir_id_devoir'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('cne', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('PS', 'PS'), ('MS', 'MS'), ('GS', 'GS'), ('CP', 'CP'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2'), ('CE6', 'CE6')], max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('ancienne_ecole', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]