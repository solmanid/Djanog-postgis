# Generated by Django 4.2.2 on 2023-06-25 10:42

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_alter_placepoints_likes_alter_placepoints_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placepoints',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]