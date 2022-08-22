
from rest_framework import serializers
from .models import Vehicle, Registration, Manufacturer, VehicleModel
#from datetime import date

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['plate', 'start_date', 'end_date']

class VehicleSerializer(serializers.ModelSerializer):
    make = serializers.CharField(source='name.make.make')
    model = serializers.CharField(source='name.name')
    type = serializers.CharField(source='name.get_type_display')
    suspension = serializers.CharField(source='get_suspension_display')
    registrations = RegistrationSerializer(many=True)
    class Meta:
        model = Vehicle
        #
        fields = [
            'make', 'model', 'type', 'registrations', 'first_registration', 'vin_number', 'axles', 'production_year', 'weight', 'gvm', 'gcwr' , 'suspension', 'active_plate', 'id',      
        ]
    
    def create(self, validated_data):
        print(validated_data)
        
        manufacturer_data = validated_data.pop('name')
        make = manufacturer_data['make']['make']
        manufacturer = Manufacturer.objects.get_or_create(make=make)
        
        model_data = manufacturer_data['name']
        type_data = manufacturer_data['get_type_display']
        t_data = None
        for t in VehicleModel.VEHICLE_TYPES:
            if str(type_data) == t[0] or str(type_data) == t[1]:
                t_data = t[0]
                break
        
        model = VehicleModel.objects.get_or_create(
            name=model_data, make=manufacturer[0], defaults={'type':t_data}
        )

        registrations_data = validated_data.pop('registrations')
        
        suspension = validated_data.pop('get_suspension_display')

        first_registration = validated_data.pop('first_registration')
        
        vehicle = Vehicle.objects.create(
            name=model[0],
            first_registration = first_registration, 
            **validated_data
        )
        for s in Vehicle.SUSPENSION_TYPES:
            if str(suspension) == s[0] or str(suspension) == s[1]:
                vehicle.suspension = s[0]
                break

        for registration_data in registrations_data:
            registrations = Registration.objects.create(vehicle=vehicle, **registration_data)
        
        return vehicle
        
    def update(self, instance, validated_data):
        
        
        # dealing with related objects
        # at the moment updating related objects via vehicle api is allowed
    
        manufacturer_data = validated_data.pop('name', None)
        
        make = manufacturer_data['make']['make']
        manufacturer = (None, None)
        manufacturer = Manufacturer.objects.get_or_create(make=make)
            
        
        model_data = manufacturer_data['name']
        type_data = manufacturer_data['get_type_display']
        
        t_data = None
        for t in VehicleModel.VEHICLE_TYPES:
            if str(type_data) == t[0] or str(type_data) == t[1]:
                t_data = t[0]
                break
        
        model = VehicleModel.objects.get_or_create(
            name=model_data, make=manufacturer[0], defaults={'type':t_data}
        )
        
        registrations_data = validated_data.pop('registrations')

        suspension = validated_data.pop('get_suspension_display')
        for s in Vehicle.SUSPENSION_TYPES:
            if str(suspension) == s[0] or str(suspension) == s[1]:
                instance.suspension = s[0]
                break
    
        # changes allowed only to start_date and end_date fields
        for registration_data in registrations_data:
            nr_plate = registration_data.get('plate')
            if nr_plate:
                registration = instance.registrations.filter(plate=nr_plate)
                if registration:
                    if 'start_date' in registration_data: 
                        registration.start_date = registration_data['start_date']
                    if 'end_date' in registration_data:
                        registration.end_date = registration_data['end_date']
                    
            

        for key, value in validated_data.items():
            if hasattr(instance, key):
                #print('insance has attr: ', key)
                setattr(instance,key, value)
            else:
                #print('instance has not attr: ', key)
                pass

        return instance