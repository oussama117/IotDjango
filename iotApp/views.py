from django.shortcuts import render,HttpResponse
from .models import cheepNecklace
# Create your views here.

def home(request):
    # context = {'allcheep':cheepNecklace.objects.all()}
    # return render(request,"iotapp/sensorDisplay.html",context=context)
    return render(request,"iotapp/sensorDisplay.html")