# Generated by Django 4.0.5 on 2022-06-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros_app', '0004_alter_membro_email_alter_membro_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='membro',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
