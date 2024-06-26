# Generated by Django 4.2.1 on 2023-06-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0007_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeRecrutement',
            fields=[
                ('idDemande', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('request', models.TextField()),
                ('cv', models.FileField(upload_to='cvs/')),
            ],
        ),
    ]
