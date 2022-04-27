# Generated by Django 2.2.13 on 2022-04-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_recipe_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='manually_carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=7, null=True, verbose_name='manually_carbohydrate'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='manually_energy',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=7, null=True, verbose_name='manually_energy'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='manually_fat',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=7, null=True, verbose_name='manually_fat'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='manually_protein',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=7, null=True, verbose_name='manually_protein'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='manually_weight',
            field=models.IntegerField(blank=True, default=None, help_text='Weight after cooking, in grams', null=True, verbose_name='manually_weight'),
        ),
        migrations.AlterField(
            model_name='recipeimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images', verbose_name='image'),
        ),
    ]
