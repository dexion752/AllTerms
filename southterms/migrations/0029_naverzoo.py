# Generated by Django 4.0.3 on 2024-07-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0028_naverocean'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverZoo',
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
                'db_table': 'naver_zoo',
                'managed': True,
            },
        ),
    ]
