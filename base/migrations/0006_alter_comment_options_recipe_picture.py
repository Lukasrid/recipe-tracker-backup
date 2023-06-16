# Generated by Django 4.2.2 on 2023-06-16 09:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_recipe_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='picture'),
        ),
    ]