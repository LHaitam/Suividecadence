# Generated by Django 4.1.3 on 2023-07-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_objectifhebdo_numero_semaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectifhebdo',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]