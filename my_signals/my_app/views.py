from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from . forms import MymodelForm
# Create your views here.
def index(request):
    user = Mymodel.objects.all()
    return render(request, 'index.html',{'user':user})

def create(request):
    form = MymodelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{"form":form})

def update(request,id):
    model = get_object_or_404(Mymodel, id=id)
    form = MymodelForm(request.POST or None,instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def delete(request,id):
    model = get_object_or_404(Mymodel,id=id)
    if request.method == 'POST':
        model.delete()
        return redirect('/')
    return render(request,'confirm_delete.html',{'model':model})