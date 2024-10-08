# Generated by Django 4.0.3 on 2024-07-31 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0042_delete_naversaju'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverSaju',
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
                'db_table': 'naver_saju',
                'managed': True,
            },
        ),
    ]
