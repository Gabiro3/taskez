# Generated by Django 4.2.7 on 2024-04-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_task_workspace'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
