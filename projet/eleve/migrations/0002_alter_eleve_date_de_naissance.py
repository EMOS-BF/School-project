# Generated by Django 4.1.1 on 2022-09-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='date_de_naissance',
            field=models.DateField(verbose_name="date de naissance de l'élève"),
        ),
    ]
