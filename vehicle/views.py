from tokenize import Token
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Vehicle, VehicleModel, Registration
import csv
import datetime
from .filters import VehicleFilter
from .forms import VehicleForm, RegistrationForm, VehicleDeleteConfirmForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .serializers import VehicleSerializer, RegistrationSerializer
from rest_framework.authentication import TokenAuthentication

@login_required
def vehicle_filter(request):
    f = VehicleFilter(request.GET, queryset=Vehicle.objects.all())

    if request.method=="POST":
        command = request.POST.get('button')
        items = list(request.POST.getlist('item'))
        if command == 'delete':
            vehicle_ids = ",".join(str(i) for i in items)
            if vehicle_ids:
                return redirect(reverse('vehicle:delete_confirm', args=[vehicle_ids]))
            else:
                messages.warning(request, 'No item selected')
        elif command == 'get-csv':
            if items:
                return export_to_csv(request, items)
            else:
                messages.warning(request, 'No item selected')
    else:
        pass

    return render(request, "vehicle/vehicle_filter.html", {'filter':f})

@login_required
def edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method=='POST':
        if pk:
            vehicle_form = VehicleForm(request.POST, instance=vehicle)
        else:
            vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
    else:
        vehicle_form = VehicleForm(instance=vehicle)

    return render(request,
                'vehicle/detail.html',
                {'vehicle_form':vehicle_form,
                'vehicle':vehicle})

@login_required
def create(request):

    if request.method == 'POST':
        vehicle_form = VehicleForm(data=request.POST)
        registration_form = RegistrationForm(data=request.POST)

        if vehicle_form.is_valid() and registration_form.is_valid():
            new_registration = registration_form.save(commit=False)
            new_vehicle = vehicle_form.save()
            new_registration.vehicle = new_vehicle
            new_registration.save()
    else:
        vehicle_form = VehicleForm()
        registration_form = RegistrationForm()
    return render(request,
                'vehicle/create.html',
                {'vehicle_form':vehicle_form,
                'registration_form':registration_form})

@login_required
def delete_confirm(request, vehicle_ids=None):

    if request.method=='POST':
        if request.POST.get('button')=='yes':

            items = vehicle_ids.split(',')
            for index in range(0, len(items)):
                try:
                    items[index] = int(items[index])
                except:
                    pass
            vehicles = Vehicle.objects.filter(pk__in=items)
            for v in vehicles:
                v.delete()
        return redirect("vehicle:vehicle_filter")
    else:
        f = VehicleDeleteConfirmForm()
    return render(request,
                    'vehicle/delete_confirm.html',
                    {'form':f, 'items':vehicle_ids})

@login_required
def registration_create(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #When adding new registration to vehicle we have to check if it should become default-active. If YES - other registration's has be marked as not active.
            if form.cleaned_data['active'] == True:
                for reg in vehicle.registrations.all():
                    reg.active = False
                    reg.save()

            registration = form.save(commit=False)
            registration.vehicle = vehicle
            registration.save()

            return redirect(reverse('vehicle:edit', args=[vehicle_id]))

    else:
        form = RegistrationForm()

    return render(request,
                    'vehicle/registration.html',
                    {'form':form}
    )

def export_to_csv(request, items):
    model = Vehicle
    queryset = Vehicle.objects.filter(pk__in=items)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vehicles.csv'
    writer = csv.writer(response)
    
    headers = ['Plates', 'Make', 'Model', 'Type','VIN', 'Production year',
                'Axles', 'Suspension']
    
    writer.writerow(headers)

    '''
    model._meta has get_fields() method but we cant't use it here becouse:
    obj.plate - it is property not field!
    have to use get_FOO_display() method
    '''
    for obj in queryset:
        data_row = []
        data_row.append(obj.plate)
        data_row.append(obj.name.make)
        data_row.append(obj.name.name)

        vmodel=VehicleModel.objects.get(pk=obj.name.id)
        data_row.append(vmodel.get_type_display())

        data_row.append(obj.vin_number)
        data_row.append(obj.production_year)
        data_row.append(obj.axles)
        data_row.append(obj.get_suspension_display())
        
        writer.writerow(data_row)
    messages.success(request, 'Success, the file was created')
    return response 

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [TokenAuthentication]
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [TokenAuthentication]

    