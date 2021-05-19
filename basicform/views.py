from django.shortcuts import render
from . import forms
# Create your views here.
def form_name_view(request):
    form=forms.ForName()
    if(request.metho=='POST'):
        form=forms.ForName(request.POST)
        
    return render(request,'basicform/form_page.html',{'form':form})