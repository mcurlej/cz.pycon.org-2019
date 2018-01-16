# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Describe what you need from us.', null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Do you need financial help from us? | Covering travel or accommodation costs etc.'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Describe what you need from us.', null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Do you need financial help from us? | Covering travel or accommodation costs etc.'),
        ),
        migrations.AlterField(
            model_name='financialaid',
            name='amount',
            field=models.CharField(help_text='How much money would you like to receive (please specify currency).', max_length=255),
        ),
        migrations.AlterField(
            model_name='financialaid',
            name='bio',
            field=models.TextField(help_text='Tell us a bit about yourself! Who you are, where you are from, and what your experience with Python is. Also include how you are involved in the Python community and how you contribute or plan to contribute to it.'),
        ),
        migrations.AlterField(
            model_name='financialaid',
            name='purpose',
            field=models.TextField(help_text='How would you like to use the granted money?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=models.TextField(help_text='Full description of your talk. How would you describe your talk to the audience?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='bio',
            field=models.TextField(help_text='Tell us a bit about yourself! Who you are, where you are from, what your experience with Python is. Be wild, be creative!'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('advanced', 'Advanced')], default='beginner', help_text='Does you talk require a high level of Python knowledge or is it suitable for everyone?', max_length=10),
        ),
        migrations.AlterField(
            model_name='talk',
            name='language',
            field=models.CharField(choices=[('en', 'English (preferred)'), ('cs', 'Czech/Slovak')], default='en', max_length=2),
        ),
        migrations.AlterField(
            model_name='talk',
            name='photo',
            field=models.ImageField(help_text=' Photo of yourself which we can publish on our website. Please use a square photo of minimum size 300 by 300 px.', upload_to='proposals/pyconcz2018/talks/', verbose_name='Your picture'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(help_text='This will be published everywhere. Make up some catchy title which will attract the audience!', max_length=200, verbose_name='Talk title'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='twitter',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='Twitter handle'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='bio',
            field=models.TextField(help_text='Tell us a bit about yourself! Who you are, where you are from, what your experience with Python is. Be wild, be creative!'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('advanced', 'Advanced')], default='beginner', help_text='Does you workshop require a high level of specialized knowledge (of Python, a library, etc.), or is it suitable for everyone?', max_length=10),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='photo',
            field=models.ImageField(help_text='Photo of yourself which we can publish on our website. Please use a square photo of minimum size 300 by 300 px.', upload_to='proposals/pyconcz2018/talks/', verbose_name='Your picture'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='twitter',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='Twitter handle'),
        ),
    ]
