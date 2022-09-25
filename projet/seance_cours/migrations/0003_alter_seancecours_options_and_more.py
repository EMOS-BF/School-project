# Generated by Django 4.1.1 on 2022-09-09 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_alter_module_nombre_heure'),
        ('seance_cours', '0002_rename_cours_seancecours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seancecours',
            options={'verbose_name': 'Liste des cours'},
        ),
        migrations.RemoveField(
            model_name='seancecours',
            name='Identifiant',
        ),
        migrations.AddField(
            model_name='seancecours',
            name='Module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module', verbose_name='Module'),
        ),
    ]