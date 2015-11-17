# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0003_auto_20150920_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('escolha', models.CharField(max_length=200)),
                ('classificacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='artigo',
            old_name='publish',
            new_name='data_publicacao',
        ),
        migrations.RenameField(
            model_name='artigo',
            old_name='contents',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='artigo',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='escolha',
            name='questao',
            field=models.ForeignKey(to='idocsapp.Artigo'),
        ),
    ]
