# Generated by Django 3.0 on 2020-03-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20200322_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='group',
            field=models.CharField(choices=[('Őrző- és terelőkutyák a svájci kutyák kivételével', 'Őrző- és terelőkutyák a svájci kutyák kivételével'), ('Pinscherek és schnauzer - molosszusok és svájci havasi kutyák', 'Pinscherek és schnauzer - molosszusok és svájci havasi kutyák'), ('Terrierek', 'Terrierek'), ('Tacskók', 'Tacskók'), ('Spiccek és őstípusú kutyák', 'Spiccek és őstípusú kutyák'), ('Kopók, vérebek és rokon fajtáik', 'Kopók, vérebek és rokon fajtáik'), ('Vizslák', 'Vizslák'), ('Spánielek, retrieverek', 'Spánielek, retrieverek'), ('Társasági és kísérőkutyák', 'Társasági és kísérőkutyák'), ('Agarak', 'Agarak'), ('FCI által nem elismert kutyafajták', 'FCI által nem elismert kutyafajták')], default='', max_length=100),
        ),
    ]
