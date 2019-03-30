# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='length',
            field=models.CharField(blank=True, choices=[('1h', '1 hour'), ('2h', '2 hours'), ('3h', '3 hours'), ('1d', 'Full day (most sprints go here!)'), ('xx', 'Something else! (Please leave a note in the abstract!)')], max_length=2),
        ),
    ]