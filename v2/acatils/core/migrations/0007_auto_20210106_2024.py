# Generated by Django 3.1.5 on 2021-01-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210105_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em:'),
        ),
        migrations.AlterField(
            model_name='news',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em:'),
        ),
    ]
