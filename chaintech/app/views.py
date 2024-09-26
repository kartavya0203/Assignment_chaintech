from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from datetime import datetime
from .models import *
# Create your views here.
def homepage(request):
    current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request,"home.html",{"current_time":current_time})
def viewdetails(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        info=Info()
        info.save()
    return render(request,'details.html',{"name":name,"email":email})