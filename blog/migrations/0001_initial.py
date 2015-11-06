# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre1', models.CharField(max_length=20)),
                ('nombre2', models.CharField(max_length=20)),
                ('apellido1', models.CharField(max_length=20)),
                ('apellido2', models.CharField(max_length=20)),
                ('fechanaci', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('experiencia', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='telefono',
            field=models.ForeignKey(to='blog.Titulo'),
        ),
    ]
