# Generated by Django 4.2.7 on 2024-04-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_remove_task_flag_alter_client_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='preferences',
            field=models.CharField(default='Productivity', max_length=120, null=True),
        ),
    ]