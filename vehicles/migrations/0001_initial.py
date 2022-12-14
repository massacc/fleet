# Generated by Django 3.2.15 on 2022-08-22 20:37

from django.db import migrations, models
import django.db.models.deletion
import vehicles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=250, verbose_name='Make')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('type', models.CharField(choices=[('1', 'Lorry'), ('2', 'Truck-tractor'), ('3', 'Ballast tractor'), ('4', 'Trailer'), ('5', 'Semi-trailer'), ('6', 'Bus'), ('0', 'Other')], max_length=10, verbose_name='Type')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_model', to='vehicles.manufacturer')),
            ],
            options={
                'verbose_name': 'Vehicle model',
                'verbose_name_plural': 'Vehicle models',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_registration', models.DateField(help_text='Date of first registratrion in Poland', verbose_name='First registatrion')),
                ('vin_number', models.CharField(help_text='Chassis number / VIN / SN number', max_length=50, unique=True, verbose_name='VIN')),
                ('axles', models.IntegerField(blank=True, default=2, null=True, verbose_name='Number of axles')),
                ('production_year', models.IntegerField(default=0)),
                ('weight', models.FloatField(blank=True, default=0, help_text='Vehicle weight (if semi-tractor)', null=True, verbose_name='Weight')),
                ('gvm', models.FloatField(blank=True, default=0, help_text='Maximum permissible laden weight', null=True, verbose_name='Gross vehicle mass')),
                ('gcwr', models.FloatField(blank=True, default=0, help_text='Maximum permissible laden weight of a vehicle combination', null=True, verbose_name='Gross combined weight rating')),
                ('suspension', models.CharField(choices=[('1', 'Air suspension'), ('2', 'Equivalent to air suspension'), ('3', 'Other')], max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle', to='vehicles.vehiclemodel', verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True, validators=[vehicles.validators.validate_future_date], verbose_name='Registration date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Deregistrarion date')),
                ('plate', models.CharField(max_length=25, verbose_name='Registration plate')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('active', models.BooleanField(default=True)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'Owner'), ('1', 'Co-owner - first named in the vehicle registration card'), ('2', 'Co-owner - second named in the vehicle registration card')], default='0', max_length=1)),
                ('percentage', models.IntegerField(default=100, verbose_name='Percentage of ownership')),
                ('purchase_date', models.DateField(verbose_name='Purchase date')),
                ('sell_date', models.DateField(blank=True, verbose_name='Date of sell')),
                ('deregistration_date', models.DateField(blank=True, verbose_name='Date of deregistration')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownerships', to='vehicles.vehicle')),
            ],
            options={
                'verbose_name': 'Ownership',
                'verbose_name_plural': 'Ownersphips',
            },
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.UniqueConstraint(fields=('plate', 'start_date'), name='unuque_plate'),
        ),
    ]
