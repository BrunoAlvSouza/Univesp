# Generated by Django 4.2 on 2023-04-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0023_alter_cadastroaluno_classe_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroaluno',
            name='professor_aluno',
            field=models.CharField(max_length=100, null=True),
        ),
    ]