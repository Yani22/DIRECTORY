# Generated by Django 3.2.9 on 2021-12-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0010_alter_enduser_suffix_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='school_year',
            field=models.DateField(default=2021),
        ),
    ]
