# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0008_auto_20151107_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='contato_email',
            field=models.EmailField(default=1, max_length=100, verbose_name=b'E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contatos',
            name='contato_tel',
            field=models.IntegerField(default=1, verbose_name=b'Telefone'),
            preserve_default=False,
        ),
    ]
