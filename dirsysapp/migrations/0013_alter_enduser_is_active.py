# Generated by Django 3.2.9 on 2021-12-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0012_enduser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
