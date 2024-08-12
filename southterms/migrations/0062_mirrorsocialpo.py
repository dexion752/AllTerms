# Generated by Django 4.0.3 on 2024-08-07 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0061_mirrorfolk'),
    ]

    operations = [
        migrations.CreateModel(
            name='MirrorSocialPo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField(blank=True, null=True)),
                ('hanJa', models.TextField(blank=True, null=True)),
                ('metaTerm1', models.TextField(blank=True, null=True)),
                ('metaTerm2', models.TextField(blank=True, null=True)),
                ('metaTerm3', models.TextField(blank=True, null=True)),
                ('simpleEx', models.TextField(blank=True, null=True)),
                ('field', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mirror_socialpo',
                'managed': True,
            },
        ),
    ]