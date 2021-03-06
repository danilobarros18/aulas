# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha_text', models.CharField(max_length=200)),
                ('boolean', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=100)),
                ('descricao_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='data de publicação')),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]
