# Generated by Django 4.1.3 on 2023-07-31 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_produit_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouvementtempsreel',
            name='soustraction',
        ),
    ]
