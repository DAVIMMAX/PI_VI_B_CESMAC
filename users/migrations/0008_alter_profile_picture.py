# Generated by Django 5.1.3 on 2024-12-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='profilepics/default.jpeg', upload_to='profilepics/'),
        ),
    ]
