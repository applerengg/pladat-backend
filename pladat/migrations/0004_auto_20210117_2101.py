# Generated by Django 3.1.4 on 2021-01-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pladat', '0003_auto_20210114_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='job_duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
