# Generated by Django 4.1.3 on 2023-07-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectifhebdo',
            name='date_debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='objectifhebdo',
            name='date_fin',
            field=models.DateField(),
        ),
    ]