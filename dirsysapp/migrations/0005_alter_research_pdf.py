# Generated by Django 3.2.9 on 2021-12-14 22:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirsysapp', '0004_alter_enduser_suffix_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='pdf',
            field=models.FileField(null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]