# Generated by Django 2.1 on 2019-04-18 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190418_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='created_date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
    ]
