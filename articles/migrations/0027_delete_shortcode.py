# Generated by Django 3.0 on 2020-03-24 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_shortcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shortcode',
        ),
    ]
