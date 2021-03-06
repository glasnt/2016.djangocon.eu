# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import organizers.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('url', organizers.fields.TwitterifyModelField(blank=True, help_text='Use @username as a twitter shortcut')),
                ('emoji', models.CharField(blank=True, max_length=10)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
