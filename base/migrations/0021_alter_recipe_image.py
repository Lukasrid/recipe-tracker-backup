# Generated by Django 4.2.2 on 2023-06-16 14:35

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=base.models.Images),
        ),
    ]
