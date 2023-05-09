# Generated by Django 4.2 on 2023-04-27 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0012_faltas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastroaluno',
            old_name='nome',
            new_name='bairro_aluno',
        ),
        migrations.RenameField(
            model_name='cadastroaluno',
            old_name='datadenascimento',
            new_name='datadenascimento_aluno',
        ),
        migrations.RenameField(
            model_name='cadastroaluno',
            old_name='ra',
            new_name='municipio_aluno',
        ),
        migrations.RenameField(
            model_name='cadastroaluno',
            old_name='rg',
            new_name='nomecompleto_aluno',
        ),
        migrations.RemoveField(
            model_name='cadastroaluno',
            name='id_aluno',
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='cpf_aluno',
            field=models.CharField(default=1, max_length=11, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='nomemae_aluno',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='nomepai_aluno',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='numero_aluno',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='rua_aluno',
            field=models.CharField(max_length=100, null=True),
        ),
    ]