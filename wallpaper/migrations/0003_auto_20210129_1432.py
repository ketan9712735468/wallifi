# Generated by Django 3.1.2 on 2021-01-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0002_auto_20210113_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='Images/'),
        ),
        migrations.AddField(
            model_name='wallpapers',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='Images/'),
        ),
    ]
