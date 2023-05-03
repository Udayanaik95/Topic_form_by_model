from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import *

# Create your views here.

def insert_data(request):
    TO=TopicForm()
    WO=WebpageForm()
    AO=AccessRecordForm()
    d={'TO':TO,'WO':WO,'AO':AO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        AFD=AccessRecordForm(request.POST)

        if TFD.is_valid() and WFD.is_valid() and AFD.is_valid():
            NSTO=TFD.save(commit=False)
            NSTO.save()

            NSWO=WFD.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()

            NSAO=AFD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()

            return HttpResponse('Data Inserted Successfully')
        else:
            return HttpResponse('Data Is Not Valid')

    return render(request,'insert_data.html',d)