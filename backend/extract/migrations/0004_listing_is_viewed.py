# Generated by Django 2.0.2 on 2018-03-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0003_auto_20180321_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]
