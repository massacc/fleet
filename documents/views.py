from django.shortcuts import render

from .models import Document
from .forms import DocumentForm
from .filters import DocumentFilter

def create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'documents/create.html', {'form':form})

def edit(request, id):
    document = Document.objects.get(pk=id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
    else:
        form = DocumentForm(instance=document)
    
    return render(request, 'documents/create.html', {'form':form})

def list(request):
    f = DocumentFilter(request.GET, queryset=Document.objects.all())

    # if request.method=="POST":
    #     command = request.POST.get('button')
    #     items = list(request.POST.getlist('item'))
    #     if command == 'delete':
    #         vehicle_ids = ",".join(str(i) for i in items)
    #         if vehicle_ids:
    #             return redirect(reverse('vehicle:delete_confirm', args=[vehicle_ids]))
    #         else:
    #             messages.warning(request, 'No item selected')
    #     elif command == 'get-csv':
    #         if items:
    #             return export_to_csv(request, items)
    #         else:
    #             messages.warning(request, 'No item selected')
    # else:
    #     pass
    
    return render(request, "documents/list.html", {'filter':f})