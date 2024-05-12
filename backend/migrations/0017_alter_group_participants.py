# Generated by Django 4.2.7 on 2024-05-12 15:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_progress_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]