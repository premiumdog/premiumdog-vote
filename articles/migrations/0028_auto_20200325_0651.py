# Generated by Django 3.0 on 2020-03-25 05:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_delete_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gdpr',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
