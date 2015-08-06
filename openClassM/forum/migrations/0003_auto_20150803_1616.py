# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150803_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenu',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='content',
            new_name='contenu',
        ),
    ]
