# Generated by Django 4.0.3 on 2024-04-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0003_naverastro_modify_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sources',
                'managed': True,
            },
        ),
    ]
