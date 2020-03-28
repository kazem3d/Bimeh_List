from django.shortcuts import render,get_object_or_404
from main.models import WorkHouse,Workers,DetailsList,MonthList
import csv
from django.http import HttpResponse
from django.db.models import Count,Sum
from django.db.models import F,BigIntegerField,ExpressionWrapper

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
    writer.writerow(['workhouse__Code','workhouse__Name','workhouse__Address',
                'year','month','worker_num','days_sum','daily_wage_sum','monthly_wage_sum','monthly_advantage',
                'monthly_wage_and_advantage',])
    # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    mon_list = MonthList.objects.all()
    mon_list=mon_list.annotate(worker_num=Count('detailslist'))
    mon_list=mon_list.annotate(days_sum=Sum('detailslist__working_days'))
    mon_list=mon_list.annotate(daily_wage_sum=Sum('detailslist__daily_wage'))
    mon_list=mon_list.annotate(monthly_wage_sum=Sum(ExpressionWrapper(F('detailslist__working_days') * F('detailslist__daily_wage') , output_field=BigIntegerField())))
    mon_list=mon_list.annotate(monthly_advantage=Sum('detailslist__advantage'))  
    
    mon_list=mon_list.annotate(monthly_wage_and_advantage=Sum(ExpressionWrapper( F('detailslist__advantage') + (F('detailslist__daily_wage') * F('detailslist__working_days')), output_field=BigIntegerField()) )) 
    mon_list=mon_list.annotate(total_wage=Sum(ExpressionWrapper( F('detailslist__advantage') + (F('detailslist__daily_wage') * F('detailslist__working_days')), output_field=BigIntegerField()) )) 
    mon_list=mon_list.annotate(bime=F('total_wage')*2)

 
    mon_list=mon_list.values_list('workhouse__Code','workhouse__Name','workhouse__Address',
                'year','month','worker_num','days_sum','daily_wage_sum','monthly_wage_sum','monthly_advantage',
                'monthly_wage_and_advantage','total_wage','workhouse__Ratio','bime'
                    )
    # print('@@@@@@@@@@@@@@@')
    # print(type(mon_list),mon_list)
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