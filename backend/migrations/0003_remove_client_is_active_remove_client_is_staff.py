# Generated by Django 4.2.7 on 2024-03-20 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_task_description_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_staff',
        ),
    ]
