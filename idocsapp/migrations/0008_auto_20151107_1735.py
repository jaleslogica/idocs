# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0007_auto_20150922_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contato_nome', models.CharField(max_length=50)),
                ('contato_nascimento', models.DateField()),
                ('contato_sexo', models.CharField(max_length=50, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])),
                ('contato_estadocivil', models.CharField(max_length=50, verbose_name=b'Estado Civil', choices=[('solteiro', 'Solteiro'), ('divorciado', 'Divorciado'), ('casado', 'Casado'), ('viuvo', 'Viuvo')])),
                ('contato_favorito', models.BooleanField(verbose_name=b'Favorito')),
            ],
        ),
        migrations.RemoveField(
            model_name='escolha',
            name='questao',
        ),
        migrations.DeleteModel(
            name='Escolha',
        ),
    ]
