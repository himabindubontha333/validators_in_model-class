from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is valid')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)
