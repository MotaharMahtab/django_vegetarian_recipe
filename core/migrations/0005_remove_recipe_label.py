# Generated by Django 2.2.13 on 2022-04-21 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220421_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='label',
        ),
    ]
