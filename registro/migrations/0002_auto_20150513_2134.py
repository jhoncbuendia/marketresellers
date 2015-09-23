# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tienda',
            name='url',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
