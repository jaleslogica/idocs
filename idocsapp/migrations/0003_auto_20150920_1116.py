# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0002_auto_20150920_0834'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Artigo',
        ),
    ]
