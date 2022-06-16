# Generated by Django 4.0.3 on 2022-06-16 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0029_registration_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'verbose_name': 'Vehicle model', 'verbose_name_plural': 'Vehicle models'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='make',
            field=models.CharField(max_length=250, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='first_registration',
            field=models.DateField(help_text='Date of first registratrion in Poland', verbose_name='First registatrion'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='gcwr',
            field=models.FloatField(blank=True, default=0, help_text='Maximum permissible laden weight of a vehicle combination', null=True, verbose_name='Gross combined weight rating'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle', to='vehicle.vehiclemodel', verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='production_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin_number',
            field=models.CharField(help_text='Chassis number / VIN / SN number', max_length=50, unique=True, verbose_name='VIN'),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='type',
            field=models.CharField(choices=[('1', 'Lorry'), ('2', 'Truck-tractor'), ('3', 'Ballast tractor'), ('4', 'Trailer'), ('5', 'Semi-trailer'), ('6', 'Bus'), ('0', 'Other')], max_length=10, verbose_name='Type'),
        ),
    ]
