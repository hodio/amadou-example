# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import example.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('audience', models.ManyToManyField(related_name=b'example_bicycle_related_audience', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, example.models.HistoryMixin),
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=100, choices=[(b'Steel', b'Steel'), (b'Titanium', b'Titatnium'), (b'Aluminum', b'Alumninum'), (b'Carbon Fiber', b'Carbon Fiber')])),
                ('paint', models.BooleanField(default=False)),
                ('audience', models.ManyToManyField(related_name=b'example_frame_related_audience', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name=b'example_frame_related_collaborators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name=b'example_frame_related_group', to='auth.Group')),
                ('owner', models.ForeignKey(related_name=b'example_frame_related_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalBicycle',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('owner_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('group_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('front_wheel_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('back_wheel_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('frame_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical bicycle',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPerson',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('owner_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('group_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('middle_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('slug', models.SlugField()),
                ('user_id', models.IntegerField(help_text=b'If the person is an existing user of your site.', null=True, db_index=True, blank=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Male'), (2, b'Female')])),
                ('avatar', models.TextField(max_length=100, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('website', models.URLField(blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('middle_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Male'), (2, b'Female')])),
                ('avatar', models.FileField(upload_to=b'avatars', blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('website', models.URLField(blank=True)),
                ('audience', models.ManyToManyField(related_name=b'example_person_related_audience', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name=b'example_person_related_collaborators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name=b'example_person_related_group', to='auth.Group')),
                ('owner', models.ForeignKey(related_name=b'example_person_related_owner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, help_text=b'If the person is an existing user of your site.', null=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
            bases=(models.Model, example.models.HistoryMixin),
        ),
        migrations.CreateModel(
            name='Scratch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('priority', models.PositiveSmallIntegerField()),
                ('audience', models.ManyToManyField(related_name=b'example_scratch_related_audience', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name=b'example_scratch_related_collaborators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name=b'example_scratch_related_group', to='auth.Group')),
                ('owner', models.ForeignKey(related_name=b'example_scratch_related_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=100, choices=[(b'Contintental', b'Continental'), (b'Michelin', b'Michelin'), (b'Bontrager', b'Bontrager')])),
                ('audience', models.ManyToManyField(related_name=b'example_tire_related_audience', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name=b'example_tire_related_collaborators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name=b'example_tire_related_group', to='auth.Group')),
                ('owner', models.ForeignKey(related_name=b'example_tire_related_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=100, choices=[(b'26', b'26 in'), (b'29', b'29 in'), (b'700', b'700cm')])),
                ('brand', models.CharField(max_length=100, choices=[(b'Mavic', b'Mavic'), (b'Shimano', b'Shimano'), (b'Power Tap', b'Power Tap')])),
                ('audience', models.ManyToManyField(related_name=b'example_wheel_related_audience', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(related_name=b'example_wheel_related_collaborators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name=b'example_wheel_related_group', to='auth.Group')),
                ('owner', models.ForeignKey(related_name=b'example_wheel_related_owner', to=settings.AUTH_USER_MODEL)),
                ('tire', models.ForeignKey(to='example.Tire')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='back_wheel',
            field=models.ForeignKey(related_name=b'example_bicycle_related_wheel_back', to='example.Wheel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicycle',
            name='collaborators',
            field=models.ManyToManyField(related_name=b'example_bicycle_related_collaborators', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicycle',
            name='frame',
            field=models.ForeignKey(to='example.Frame'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicycle',
            name='front_wheel',
            field=models.ForeignKey(related_name=b'example_bicycle_related_wheel_front', to='example.Wheel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicycle',
            name='group',
            field=models.ForeignKey(related_name=b'example_bicycle_related_group', to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bicycle',
            name='owner',
            field=models.ForeignKey(related_name=b'example_bicycle_related_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
