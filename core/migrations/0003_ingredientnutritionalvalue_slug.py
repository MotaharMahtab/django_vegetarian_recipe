# Generated by Django 2.2.13 on 2022-04-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220420_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientnutritionalvalue',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]