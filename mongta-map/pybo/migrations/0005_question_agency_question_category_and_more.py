# Generated by Django 4.0.1 on 2022-01-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_rename_data_format_question_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='agency',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='update_date',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]