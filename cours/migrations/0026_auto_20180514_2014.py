# Generated by Django 2.0.4 on 2018-05-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0025_auto_20180514_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
