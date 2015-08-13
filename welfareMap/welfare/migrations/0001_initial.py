# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Welfare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('address', models.TextField()),
                ('content', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('urgent', models.CharField(max_length=10)),
                ('helpType', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('helpUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='helpUser', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user')),
            ],
        ),
    ]
