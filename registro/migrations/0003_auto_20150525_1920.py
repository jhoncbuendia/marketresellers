# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registro', '0002_auto_20150513_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='tienda',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pais',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
