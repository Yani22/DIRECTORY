# Generated by Django 3.2.9 on 2021-12-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0013_alter_enduser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
