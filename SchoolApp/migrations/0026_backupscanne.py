# Generated by Django 4.2.1 on 2023-10-07 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0025_useranalytics'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackUpScanne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('CNE_eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.eleve')),
                ('Id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.agent')),
            ],
        ),
    ]
