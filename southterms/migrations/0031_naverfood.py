# Generated by Django 4.0.3 on 2024-07-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0030_navermicrobio'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverFood',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('term', models.TextField(blank=True, null=True)),
                ('eng', models.TextField(blank=True, null=True)),
                ('simple_sense', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'naver_food',
                'managed': True,
            },
        ),
    ]
