# Generated by Django 4.0.3 on 2024-07-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0019_naverchemipedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='sources',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
    ]