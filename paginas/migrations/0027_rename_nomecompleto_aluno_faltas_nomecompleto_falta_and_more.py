# Generated by Django 4.2 on 2023-04-29 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0026_alter_faltas_presenca_falta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faltas',
            old_name='nomecompleto_aluno',
            new_name='nomecompleto_falta',
        ),
        migrations.RenameField(
            model_name='faltas',
            old_name='turma_aluno',
            new_name='turma_falta',
        ),
    ]
