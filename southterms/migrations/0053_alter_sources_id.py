# Generated by Django 4.0.3 on 2024-08-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0052_alter_sources_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sources',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
