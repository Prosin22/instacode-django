# Generated by Django 2.0.3 on 2018-04-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_auto_20180401_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapitre',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
