# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-24 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0031_auto_20160921_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['value']},
        ),
        migrations.AlterField(
            model_name='registration',
            name='student_number',
            field=models.CharField(max_length=8),
        ),
    ]