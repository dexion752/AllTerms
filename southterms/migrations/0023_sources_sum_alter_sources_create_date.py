# Generated by Django 4.0.3 on 2024-07-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('southterms', '0022_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='sources',
            name='sum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sources',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]