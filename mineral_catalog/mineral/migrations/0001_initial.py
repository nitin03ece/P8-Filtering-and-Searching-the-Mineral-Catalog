# Generated by Django 2.1.5 on 2019-03-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_filename', models.TextField()),
                ('image_caption', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('formula', models.TextField()),
                ('strunz_classification', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('crystal_system', models.CharField(max_length=255)),
                ('unit_cell', models.TextField()),
                ('crystal_symmetry', models.TextField()),
                ('cleavage', models.TextField()),
                ('mohs_scale_hardness', models.TextField()),
                ('luster', models.TextField()),
                ('streak', models.CharField(max_length=255)),
                ('diaphaneity', models.CharField(max_length=255)),
                ('optical_properties', models.TextField()),
                ('refractive_index', models.TextField()),
                ('crystal_habit', models.TextField()),
                ('specific_gravity', models.TextField()),
                ('group', models.CharField(max_length=255)),
            ],
        ),
    ]