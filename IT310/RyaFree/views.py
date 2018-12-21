from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from RyaFree.forms import NewOption
# Create your views here.

def index(request):
    #my_dict = {'insert_me':"Hello , this is from first app index"}
    return render (request,'RyaFree/InitialDesign.html')#context=my_dict)
    #return HttpResponse("<em>Are you free?<em>")
def help(request):
    helpdict = {'help_insert':"Run, help isn't coming."}
    return render(request,'RyaFree/help.html',context =helpdict)

def Services(request):
    return render (request,'RyaFree/Services.html')

def Poll(request):
    return render (request,'RyaFree/poll.html')

def Options(request):

    form = NewOption()

    if request.method == "POST":
        form = NewOption(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form INvalid')
    return render(request,"RyaFree/poll.html",{'form':form})

def form_name_view(request):
    form = forms.FreeForm()
    return render(request,'RyaFree/poll.html',{'form':form})
