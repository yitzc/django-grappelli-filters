# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name', 'first_name')},
        ),
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ('-year', 'name')},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title', 'author')},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('name',)},
        ),
    ]