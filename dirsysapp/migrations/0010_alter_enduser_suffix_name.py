# Generated by Django 3.2.9 on 2021-12-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0009_auto_20211218_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='suffix_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
