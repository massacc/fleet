# Generated by Django 4.0.1 on 2022-02-13 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_documentvehicle_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentvehicle',
            name='axles',
            field=models.IntegerField(blank=True, default=0.0, verbose_name='Number of axles'),
        ),
        migrations.AlterField(
            model_name='documentvehicle',
            name='gcwr',
            field=models.FloatField(blank=True, default=0.0, help_text='maximum permissible laden weight of a vehicle combination', verbose_name='Gross combined weight rating'),
        ),
        migrations.AlterField(
            model_name='documentvehicle',
            name='gvm',
            field=models.FloatField(blank=True, default=0.0, help_text='Maximum permissible laden weight', verbose_name='Gross vehicle mass'),
        ),
        migrations.AlterField(
            model_name='documentvehicle',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, help_text='Vehicle weight (if semi-tractor)', verbose_name='Weight'),
        ),
    ]
