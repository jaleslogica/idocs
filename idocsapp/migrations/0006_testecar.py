# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idocsapp', '0005_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lista_de_carro', models.ForeignKey(to='idocsapp.Car')),
            ],
        ),
    ]
