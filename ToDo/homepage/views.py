from django.shortcuts import render,redirect
import datetime
from homepage.models import Reminder
# Create your views here.
def home(request):
    print(Reminder.objects.all())
    context={
        'Description':Reminder.objects.all()
    };
    if request.method=="POST":
        reminder=request.POST['newitem']
        dateNow=datetime.datetime.now()
        row=Reminder(remind=reminder,date=dateNow)
        row.save()
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)
def delete(request):
    
