# Generated by Django 4.0.4 on 2022-07-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_entrada', models.TimeField()),
                ('horario_saida', models.TimeField()),
                ('turno', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], max_length=50)),
                ('dia_semana', models.CharField(choices=[('Segunda-Feira', 'Segunda-Feira'), ('Terça-Feira', 'Terça-Feira'), ('Quarta-Feira', 'Quarta-Feira'), ('Quinta-Feira', 'Quinta-Feira'), ('Sexta-Feira', 'Sexta-Feira'), ('Sabádo', 'Sabádo'), ('Domingo', 'Domingo')], max_length=50)),
            ],
        ),
    ]
