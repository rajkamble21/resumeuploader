# Generated by Django 4.1.2 on 2022-10-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_jon_city_resume_job_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
