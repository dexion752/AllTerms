# Generated by Django 4.0.3 on 2024-04-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='naverastro',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
