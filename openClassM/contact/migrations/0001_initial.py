# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('auteur', models.CharField(max_length=42)),
                ('content', models.TextField(max_length=10000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
