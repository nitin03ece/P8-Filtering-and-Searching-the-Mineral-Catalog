# Generated by Django 2.1.5 on 2019-03-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral', '0009_remove_mineral_image_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='image_filename',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
