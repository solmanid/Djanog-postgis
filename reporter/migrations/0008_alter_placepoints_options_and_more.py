# Generated by Django 4.2.2 on 2023-06-28 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reporter', '0007_alter_placepoints_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placepoints',
            options={'default_permissions': ['add', 'change', 'delete'], 'permissions': (('view_placepoints', 'Can view place points'),)},
        ),
        migrations.CreateModel(
            name='PlacePointsUserObjectPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.placepoints')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'permission', 'content_object')},
            },
        ),
        migrations.CreateModel(
            name='PlacePointsGroupObjectPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.placepoints')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
            ],
            options={
                'abstract': False,
                'unique_together': {('group', 'permission', 'content_object')},
            },
        ),
        migrations.CreateModel(
            name='BigUserObjectPermission',
            fields=[
                ('object_pk', models.CharField(max_length=255, verbose_name='object ID')),
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'indexes': [models.Index(fields=['content_type', 'object_pk'], name='reporter_bi_content_4f5b92_idx'), models.Index(fields=['content_type', 'object_pk', 'user'], name='reporter_bi_content_476027_idx')],
                'unique_together': {('user', 'permission', 'object_pk')},
            },
        ),
        migrations.CreateModel(
            name='BigGroupObjectPermission',
            fields=[
                ('object_pk', models.CharField(max_length=255, verbose_name='object ID')),
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
            ],
            options={
                'abstract': False,
                'indexes': [models.Index(fields=['content_type', 'object_pk'], name='reporter_bi_content_8dd04f_idx'), models.Index(fields=['content_type', 'object_pk', 'group'], name='reporter_bi_content_598b1d_idx')],
                'unique_together': {('group', 'permission', 'object_pk')},
            },
        ),
    ]
