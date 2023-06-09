# Generated by Django 4.2 on 2023-04-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0011_notas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faltas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('ra', models.CharField(max_length=100, null=True)),
                ('bimestre1_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bimestre2_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bimestre3_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bimestre4_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bimestre5_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bimestre6_faltas', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
