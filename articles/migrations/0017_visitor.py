# Generated by Django 3.0 on 2020-03-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_remove_article_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]