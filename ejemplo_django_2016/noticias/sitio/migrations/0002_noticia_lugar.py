# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='lugar',
            field=models.CharField(default=b'Aca', max_length=50),
        ),
    ]
