# Generated by Django 4.1 on 2022-08-28 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_alter_profile_profile_about_me'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_followers',
            new_name='followers',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_following',
            new_name='following',
        ),
    ]