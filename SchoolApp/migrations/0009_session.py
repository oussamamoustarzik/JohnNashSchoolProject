# Generated by Django 4.2.1 on 2023-06-05 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0008_demanderecrutement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.professeur')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe')),
            ],
        ),
    ]
