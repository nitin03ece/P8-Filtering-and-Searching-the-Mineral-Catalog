# Generated by Django 2.1.5 on 2019-03-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineral', '0004_auto_20190316_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
