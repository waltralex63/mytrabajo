# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='titulo',
            field=models.ForeignKey(to='blog.Titulo'),
        ),
    ]
