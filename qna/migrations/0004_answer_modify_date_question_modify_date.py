# Generated by Django 4.0.3 on 2024-01-29 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
