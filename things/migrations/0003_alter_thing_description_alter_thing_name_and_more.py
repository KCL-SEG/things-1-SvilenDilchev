# Generated by Django 4.2.7 on 2023-11-03 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_thing_description_thing_name_thing_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, default='', max_length=120, validators=[django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.TextField(default='', max_length=30, unique=True, validators=[django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
