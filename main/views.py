from django.shortcuts import render,get_object_or_404
from main.models import WorkHouse,Workers,DetailsList,MonthList

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

def month_list(request):

    months_list=MonthList.objects.all()

    context={

        'months_list':months_list


    }
    
    return render(request,'main/month_list.html',context)

def details_list(request,list_id):

    # records=get_object_or_404(DetailsList,pk=list_id) 
    records= DetailsList.objects.filter(month_list__pk=list_id)

    context={

        'records': records

    }    

    return render (request,'main/details_list.html',context)