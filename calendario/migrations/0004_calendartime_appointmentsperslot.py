# Generated by Django 2.1.3 on 2019-02-10 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_auto_20190209_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendartime',
            name='appointmentsPerSlot',
            field=models.IntegerField(default=1, verbose_name='Máximo número de citas por tramo'),
        ),
    ]
