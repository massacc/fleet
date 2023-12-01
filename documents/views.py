from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Document
from .forms import DocumentForm, DeleteForm
from .filters import DocumentFilter
#from vehicles.forms import PlatesForm
from vehicles.models import Registration

def create(request):
    plates = Registration.objects.filter(active=True)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request,"File uploaded")
        else:
            messages.error(request, "File uploading failed")
    else:
        form = DocumentForm()
    return render(request, 'documents/create.html', {'form':form, 'plates':plates})

def edit(request, id):
    document = Document.objects.get(pk=id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
    else:
        form = DocumentForm(instance=document)
    
    if form.is_valid():
        form.save()
    
    return render(request, 'documents/create.html', {'form':form})

def doc_list(request):
    print(request)
    f = DocumentFilter(request.GET, queryset=Document.objects.all())

    if request.method=="POST":
        command = request.POST.get('button')
        items = list(request.POST.getlist('item'))
        if command == 'delete':
            ids = ",".join(str(i) for i in items)
            if ids:
                return redirect(reverse('documents:delete', args=[ids]))
            else:
                messages.warning(request, 'No item selected')
        # elif command == 'get-csv':
        #     if items:
        #         return export_to_csv(request, items)
        #     else:
        #         messages.warning(request, 'No item selected')
    else:
        pass
    
    return render(request, "documents/list.html", {'filter':f})

def delete(request, ids=None):
    
    if request.method=='POST':
        if request.POST.get('button')=='yes':
            try:
                items = ids.split(',')
                for index in range(0, len(items)):
                    items[index] = int(items[index])
                documents = Document.objects.filter(pk__in=items)
                for d in documents:
                    d.delete()
                messages.success(request,'Deleted')
            except Exception as e:
                messages.error(request, 'Document(s) deleting failed')
            
        return redirect('documents:documents')
    else:
        f = DeleteForm()
    return render(request,
                    'documents/delete.html',
                    {'form':f, 'items':ids})
