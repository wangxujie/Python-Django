# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog2', '0005_person_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1, null=True, verbose_name='\u72b6\u6001'),
        ),
    ]
