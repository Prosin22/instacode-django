# Generated by Django 2.0.3 on 2018-04-03 11:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0003_auto_20180401_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapitre',
            name='intro',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='cours',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='probleme',
            field=tinymce.models.HTMLField(),
        ),
    ]
