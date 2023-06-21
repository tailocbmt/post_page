# Generated by Django 4.0 on 2023-06-20 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('title', models.CharField(max_length=256)),
                ('author_name', models.CharField(max_length=120)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author_name', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(db_column='post_id', max_length=36, on_delete=django.db.models.deletion.CASCADE, to='post_list.post')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]