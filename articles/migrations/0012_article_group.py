# Generated by Django 3.0 on 2020-03-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20200320_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='group',
            field=models.CharField(choices=[('Őrző- és terelőkutyák a svájci kutyák kivételével', '1'), ('Pinscherek és schnauzer - molosszusok és svájci havasi kutyák', '2'), ('Terrierek', '3'), ('Tacskók', '4'), ('Spiccek és őstípusú kutyák', '5'), ('Kopók, vérebek és rokon fajtáik', '6'), ('Vizslák', '7'), ('Spánielek, retrieverek', '8'), ('Társasági és kísérőkutyák', '9'), ('Agarak', '10')], default='', max_length=100),
        ),
    ]
