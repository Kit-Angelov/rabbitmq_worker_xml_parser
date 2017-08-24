# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rabbit_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rabbit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rabbit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]