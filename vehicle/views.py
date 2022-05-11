from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Vehicle, Registration, VehicleModel, Manufacturer
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory
from django_filters.views import FilterView
from .filters import VehicleFilter
from .forms import VehicleForm, RegistrationForm, VehicleDeleteConfirmForm

def vehicle_edit(request, pk=None):
    VehicleFormSet = inlineformset_factory(VehicleModel, Vehicle, exclude=('id',), extra=2)
    vehicle = VehicleModel.objects.get(pk=pk)
    formset = VehicleFormSet(instance=vehicle)
    if request.method=='POST':
        formset = VehicleFormSet(request.POST, request.FILES, instance=vehicle)
        formset.save()

    return render(request,
                'vehicle/edit.html',
                {'formset':formset,
                'object':vehicle})


def vehicle_detail(request, pk):
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
def registration_list(request, pk):
    # formset is not proper solution !!!
    # using it in these function just as formset practice
    vehicle = Vehicle.objects.get(id=pk)
    queryset=Registration.objects.filter(vehicle=vehicle)
    RegistrationFormSet = modelformset_factory(Registration,
                            fields=('plate', 'start_date', 'end_date'),
                            extra=1,
                            can_delete=False,
                            can_delete_extra=False)
    if request.method == 'POST':

        formset = RegistrationFormSet(request.POST, request.FILES,queryset=queryset)
        if formset.is_valid():
            print('>>>> FORMSET.IS_VALID<<<<<')
            #formset.save()
            instances = formset.save()
            #for obj in formset.deleted_objects:
            #    obj.delete()
            for f in instances:
                if not f.vehicle:
                    f.vehicle = vehicle
                    f.save()
                    print('pojazd', f.vehicle)
            redirect(reverse('vehicle:registration_list', args=[pk]))

        else:
            print('IS NOT VALID', formset.errors)
    else:
        formset = RegistrationFormSet(queryset=queryset
                )

    return render(request,
                    'vehicle/registration.html',
                    {'formset':formset,
                    'id':pk}
    )
def plate_list(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    RegistrationInlineFormSet = inlineformset_factory(
                                    Vehicle,
                                    Registration,
                                    fields=('plate', 'start_date', 'end_date', 'active'),
                                    extra=1,
                                    can_delete=True,
                                    can_delete_extra=False)
    if request.method=='POST':
        formset = RegistrationInlineFormSet(
                                    request.POST,
                                    request.FILES,
                                    instance=vehicle)
        if formset.is_valid():
            formset.save()
            return redirect(vehicle.get_absolute_url())

    else:
        formset = RegistrationInlineFormSet(instance=vehicle)

    return render(request,
                'vehicle/plates.html',
                {'formset':formset})

def vehicle_filter(request):
    f = VehicleFilter(request.GET, queryset=Vehicle.objects.all())

    if request.method=="POST":
        command = request.POST.get('button')


        items = list(request.POST.getlist('item'))
        print('itemsy przekazane', items)
        if command == 'delete':
            #for vehicle in Vehicle.objects.filter(pk__in=items):
            #    vehicle.delete()
            #f = VehicleFilter(request.GET, queryset=Vehicle.objects.all())
            vehicle_ids = ",".join(str(i) for i in items)
            return redirect(reverse('vehicle:delete_confirm', args=[vehicle_ids]))
    else:
        pass

    return render(request, "vehicle/vehicle_filter.html", {'filter':f})

########## funkcja testowa #########################
def document_list(request):
    documents = DocumentVehicle.objects.all()




    if request.method=='POST':
        selected_items = [key for key in request.POST if key not in ['csrfmiddlewaretoken', 'delete', 'download']]
        print(request.POST)
        if 'delete' in request.POST:
            pass
            #print('elementy do usunięcia')
            #print(selected_items)
        elif 'download' in request.POST:
            pass
            #print('elementy do pobranoa')
            #print(selected_items)


    else:
        pass


    return render(request, 'vehicle/document_list.html',
                    {'documents':documents})


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle/create.html'
    context_object_name = 'vehicle'
    fields = ['name', 'registration', 'registration_date', 'vin_number', 'axles', 'production_year', 'suspension']
    success_url = reverse_lazy('vehicle:vehicle_filter')
'''
def vehicle_crud(request, vehicle_id):
    vehicle = get_object_or_404(DocumentVehicle, id=vehicle_id)

    if request.method = 'POST':
        form =
'''


def document(request):
    return render(request,
                    'dt1/dt1p1.html')

def document_list_filter(request):
    f = VehicleFilter(request.GET, queryset=Vehicle.objects.all())




    if request.method=='POST':
        selected_items = [key for key in request.POST if key not in ['csrfmiddlewaretoken', 'delete', 'download']]
        print(request.POST)
        if 'delete' in request.POST:
            pass
            #print('elementy do usunięcia')
            #print(selected_items)
        elif 'download' in request.POST:
            pass
            #print('elementy do pobranoa')
            #print(selected_items)


    else:
        pass


    return render(request, 'vehicle/document_list2.html',
                    {'filter':f})
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

def delete_confirm(request, vehicle_ids=None):

    if request.method=='POST':
        print('jest post')
        print('jtest ', request.POST.get('button'))
        if request.POST.get('button')=='yes':

            items = vehicle_ids.split(',')
            for index in range(0, len(items)):
                try:
                    items[index] = int(items[index])
                except:
                    pass
            print('######### itemsy: ', items)
            vehicles = Vehicle.objects.filter(pk__in=items)
            for v in vehicles:
                print('aksuje pojazd')
                v.delete()
        return redirect("vehicle:vehicle_filter")
    else:
        f = VehicleDeleteConfirmForm()
    return render(request,
                    'vehicle/delete_confirm.html',
                    {'form':f, 'items':vehicle_ids}
                    )

