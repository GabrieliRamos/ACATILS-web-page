# Generated by Django 3.1.5 on 2021-01-16 00:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210115_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Criado em:'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Criado em:'),
        ),
    ]
