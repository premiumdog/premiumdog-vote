# Generated by Django 3.0 on 2020-03-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20200321_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='group',
            field=models.CharField(choices=[('Őrző- és terelőkutyák a svájci kutyák kivételével', 'Őrző- és terelőkutyák a svájci kutyák kivételével'), ('2', 'Pinscherek és schnauzer - molosszusok és svájci havasi kutyák'), ('3', 'Terrierek'), ('4', 'Tacskók'), ('5', 'Spiccek és őstípusú kutyák'), ('6', 'Kopók, vérebek és rokon fajtáik'), ('7', 'Vizslák'), ('8', 'Spánielek, retrieverek'), ('9', 'Társasági és kísérőkutyák'), ('10', 'Agarak'), ('11', 'FCI által nem elismert kutyafajták')], default='', max_length=100),
        ),
    ]
