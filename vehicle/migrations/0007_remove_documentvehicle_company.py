# Generated by Django 4.0.1 on 2022-02-17 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_alter_documentvehicle_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentvehicle',
            name='company',
        ),
    ]
