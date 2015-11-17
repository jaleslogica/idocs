# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0004_auto_20150920_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('photo', models.ImageField(upload_to=b'cars')),
            ],
        ),
    ]
