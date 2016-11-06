# Generated by Django 1.10.3 on 2016-11-06 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
            ],
        ),
    ]
