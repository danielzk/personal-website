# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-29 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import utils.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(editable=False, null=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'verbose_name': 'Message',
            },
            bases=(utils.models.ValidationModelMixin, utils.models.TimeStampedSaveModelMixin, models.Model),
        ),
    ]