# Generated by Django 2.1 on 2018-11-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181112_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pattern_name',
            new_name='urlpattern_name',
        ),
    ]
