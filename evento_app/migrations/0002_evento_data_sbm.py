# Generated by Django 3.2.13 on 2022-05-16 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evento_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data_sbm',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
