# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150803_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contenu',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='contenu',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='titre',
            new_name='title',
        ),
    ]
