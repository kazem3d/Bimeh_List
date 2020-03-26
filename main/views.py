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



def export_workhouse_data(request):

    #this section for .csv files

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="kar_list.txt"'

    writer = csv.writer(response)
    # writer.writerow(['header names list'])
    mon_list = MonthList.objects.all().values_list()
    
    writer.writerow(mon_list)    
    return response


    #this section is for .txt files

    # text_file_content='salam'
    # response = HttpResponse(text_content ,content_type='text/plain')
    # return response

def export_workers_data(request):

    #this section for .csv files

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="work_list.txt"'

    writer = csv.writer(response)
    # writer.writerow(['header names list'])
    workers_list = DetailsList.objects.all().values_list()
    for worker in workers_list:
        writer.writerow(worker)    
    return response