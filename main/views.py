from django.shortcuts import render,get_object_or_404
from main.models import WorkHouse,Workers,DetailsList,MonthList
import csv
from django.http import HttpResponse

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



def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment;  filename="users.csv"'

    # writer2=open('test.txt','w')
    writer = csv.writer(response)
    writer.writerow(['Username'])
    users = WorkHouse.objects.all().values_list('Code')
    
    for user in users:
        writer.writerow(user)    
    return response