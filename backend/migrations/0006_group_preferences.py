# Generated by Django 4.2.7 on 2024-03-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_group_participants_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='preferences',
            field=models.CharField(max_length=120, null=True),
        ),
    ]