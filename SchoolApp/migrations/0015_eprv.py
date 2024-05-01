# Generated by Django 4.2.1 on 2023-06-08 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0014_devoircontenue_homework_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eprv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe')),
                ('epreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.epreuve')),
            ],
        ),
    ]
