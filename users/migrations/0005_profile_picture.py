# Generated by Django 5.1.3 on 2024-12-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='media/images/default.jpeg', upload_to='media/images'),
        ),
    ]