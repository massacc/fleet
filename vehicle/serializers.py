from rest_framework import serializers
from .models import Vehicle, Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['plate', 'start_date', 'end_date'
        ]

class VehicleSerializer(serializers.ModelSerializer):
    make = serializers.CharField(source='name.make.make')
    model = serializers.CharField(source='name.name')
    type = serializers.CharField(source='name.get_type_display')
    suspension = serializers.CharField(source='get_suspension_display')
    registrations = RegistrationSerializer(many=True)
    class Meta:
        model = Vehicle
        fields = [
            'plate', 'make', 'model', 'registrations', 'type', 'first_registration', 'vin_number', 'axles', 'production_year', 'weight', 'gvm', 'gcwr', 'suspension'         
        ]