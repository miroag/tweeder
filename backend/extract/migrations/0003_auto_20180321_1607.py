# Generated by Django 2.0.2 on 2018-03-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0002_auto_20180321_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='view_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date viewed'),
        ),
    ]
