# Generated by Django 4.2 on 2023-04-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0019_rename_data_faltas_data_faltas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroaluno',
            name='id_aluno',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastroaluno',
            name='cpf_aluno',
            field=models.CharField(max_length=11),
        ),
    ]
