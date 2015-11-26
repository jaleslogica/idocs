# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0009_auto_20151107_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='contato_bairro',
            field=models.CharField(default=10, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contatos',
            name='contato_cidade',
            field=models.CharField(default=11, help_text=b'Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Belo Horizonte', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contatos',
            name='contato_endereco',
            field=models.CharField(default=12, help_text=b'Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Rua Martinho Estrela,  1229', max_length=255, verbose_name='Endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contatos',
            name='contato_estado',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[('ce', 'CE'), ('pb', 'PB'), ('sp', 'SP'), ('rj', 'RJ')]),
        ),
        migrations.AddField(
            model_name='contatos',
            name='contato_position',
            field=geoposition.fields.GeopositionField(default=12, help_text=b'Nao altere os valores calculados automaticamente de latitude e longitude', max_length=42, verbose_name='Geolocalizacao'),
            preserve_default=False,
        ),
    ]
