# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('English', models.FloatField()),
                ('Science', models.FloatField()),
                ('social', models.FloatField()),
                ('maths', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolresults.student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolresults.semester'),
        ),
    ]
