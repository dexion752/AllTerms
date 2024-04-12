# Generated by Django 4.0.3 on 2024-04-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaverAstro',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('term', models.TextField(blank=True, null=True)),
                ('eng', models.TextField(blank=True, null=True)),
                ('simple_sense', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'naver_astro',
                'managed': True,
            },
        ),
    ]
