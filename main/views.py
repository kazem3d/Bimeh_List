from django.shortcuts import render
from main.models import WorkHouse,Workers

def home(request):
    return render(request,"main/home.html")


def workers_list(request):

    workers=Workers.objects.all()

    context={
        'workers':workers
    }

    return render(request,"main/workers_list.html",context)

def workhouses_list(request):
    workhouses=WorkHouse.objects.all()

    context={
        'workhouses':workhouses
    }

    return render(request,'main/workhouse_list.html',context)

