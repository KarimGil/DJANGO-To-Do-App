from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)


        if form.is_valid():
            form.save()
            items = List.objects.all
            messages.success(request,'Task has been added to List!')
            return render(request,'home.html',{'items':items})
        
        else:
            return redirect('home')


            


    else:
        items = List.objects.all
        return render(request,'home.html',{'items':items})
def about(request):
    return render(request,'about.html',{})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,'Task has been deleted from the List!')
    return redirect('home')

def task_done(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def task_notdone(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)


        if form.is_valid():
            form.save()
            items = List.objects.all
            messages.success(request,'Task has been Edited to List!')
            return redirect('home')
        
        else:
            return redirect('edit')

    else:
        item = List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})


    

