# Generated by Django 4.2 on 2023-04-21 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0009_alter_notas_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notas',
        ),
    ]