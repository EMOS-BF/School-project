# Generated by Django 4.0.2 on 2022-10-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='nom',
            field=models.CharField(max_length=200, null=True, verbose_name="INE de l'élève"),
        ),
    ]
