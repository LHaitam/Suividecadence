# Generated by Django 4.1.3 on 2023-07-20 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_objectifhebdo_numero_semaine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectifhebdo',
            name='numero_semaine',
        ),
    ]
