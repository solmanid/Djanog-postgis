# Generated by Django 4.2.2 on 2023-06-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_alter_placepoints_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='placepoints',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
