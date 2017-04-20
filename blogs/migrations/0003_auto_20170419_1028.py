# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 10:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_pub_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pub_time', models.DateTimeField(default=datetime.datetime(2017, 4, 19, 10, 28, 27, 235102, tzinfo=utc))),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 19, 10, 28, 27, 232461, tzinfo=utc)),
        ),
    ]