# Generated by Django 3.1.5 on 2021-03-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210301_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='translation',
            field=models.TextField(blank=True, verbose_name='Tradução para LIBRAS (link YouTube)'),
        ),
    ]
