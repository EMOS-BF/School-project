# Generated by Django 4.1.1 on 2022-09-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='nombre_heure',
            field=models.PositiveIntegerField(verbose_name='Nombre heure du module'),
        ),
    ]
