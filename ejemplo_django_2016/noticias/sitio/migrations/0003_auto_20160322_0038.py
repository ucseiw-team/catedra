# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_noticia_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(blank=True, to='sitio.Categoria', null=True),
        ),
    ]
