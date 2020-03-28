# Generated by Django 3.0 on 2020-03-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_auto_20200325_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('body', models.TextField()),
            ],
        ),
    ]
