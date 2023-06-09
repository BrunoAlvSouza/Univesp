# Generated by Django 4.2 on 2023-05-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0032_alter_notas_datahoje_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastroprofessor',
            fields=[
                ('id_professor', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cpf_professor', models.CharField(max_length=11)),
                ('nomecompleto_professor', models.CharField(max_length=100, null=True)),
                ('datadenascimento_professor', models.DateField(null=True)),
                ('rua_professor', models.CharField(max_length=100, null=True)),
                ('numero_professor', models.CharField(max_length=100, null=True)),
                ('bairro_professor', models.CharField(max_length=100, null=True)),
                ('municipio_professor', models.CharField(max_length=100, null=True)),
                ('formacao_professor', models.CharField(max_length=100, null=True)),
                ('email_professor', models.EmailField(max_length=254, null=True)),
                ('classe_professor', models.CharField(choices=[(1, 'turma1'), (2, 'turma2'), (3, 'turma3'), (4, 'turma4'), (5, 'turma5'), (6, 'turma6')], max_length=100, null=True)),
            ],
        ),
    ]
