# Generated by Django 5.1.2 on 2024-11-26 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Post',
        ),
    ]