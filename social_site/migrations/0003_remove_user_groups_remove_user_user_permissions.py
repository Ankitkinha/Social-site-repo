# Generated by Django 4.2.13 on 2024-06-13 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_site', '0002_user_groups_user_is_active_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
