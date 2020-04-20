
from django.shortcuts import render,get_object_or_404
from main.models import WorkHouse,Workers,DetailsList,MonthList

import csv
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count,Sum
from django.db.models import F,BigIntegerField,ExpressionWrapper,CharField,Value
from main.choices import city_choice,job_choice
from main.forms import WorkhouseForm,WorkersForm,MonthlistForm,DetailsForm
import codecs
from main import iransystem

def reverse(s):
    return s[::-1]

codecs.register(lambda e: iransystem.getregentry())

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

    response = HttpResponse(content_type='text/csv ;charset=iransystem')
    response['Content-Disposition'] = 'attachment;  filename="kar_list.txt"'

    writer = csv.writer(response)

    
    # writer.writerow(['workhouse__Code','workhouse__Name','workhouse__Address',
    #             'year','month','worker_num','days_sum','daily_wage_sum','monthly_wage_sum','monthly_advantage',
    #             'monthly_wage_and_advantage',])
    # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    
    mon_list =MonthList.objects.all()

    mon_list=mon_list.annotate(worker_num=Count('detailslist'))
    mon_list=mon_list.annotate(days_sum=Sum('detailslist__working_days'))
    mon_list=mon_list.annotate(daily_wage_sum=Sum('detailslist__daily_wage'))
    mon_list=mon_list.annotate(monthly_wage_sum=Sum(ExpressionWrapper(F('detailslist__working_days') * F('detailslist__daily_wage') , output_field=BigIntegerField())))
    mon_list=mon_list.annotate(monthly_advantage=Sum('detailslist__advantage'))  

    mon_list=mon_list.annotate(monthly_wage_and_advantage=Sum(ExpressionWrapper( F('detailslist__advantage') + (F('detailslist__daily_wage') * F('detailslist__working_days')), output_field=BigIntegerField()) )) 
    mon_list=mon_list.annotate(total_wage=Sum(ExpressionWrapper( F('detailslist__advantage') + (F('detailslist__daily_wage') * F('detailslist__working_days')), output_field=BigIntegerField()) )) 

    mon_list=mon_list.annotate(employer_share_sum=ExpressionWrapper(F('total_wage')*0.2,output_field=BigIntegerField()  ))
    mon_list=mon_list.annotate(insured_share_sum=ExpressionWrapper(F('total_wage')*0.07,output_field=BigIntegerField()  ))
    mon_list=mon_list.annotate(unemployment_premium_sum=ExpressionWrapper(F('total_wage')*0.03,output_field=BigIntegerField()  ))
    mon_list=mon_list.annotate(list_number=Value('01', CharField()))
    mon_list=mon_list.annotate(list_type=Value('0', CharField()))
    mon_list=mon_list.annotate(list_description=Value('2', CharField()))
    mon_list=mon_list.annotate(porsantaj_ratio=Value('0', CharField()))
    mon_list=mon_list.annotate(hard_ratio=Value('0', CharField()))


    # mon_list=mon_list.extra(select = {'list_number': 0})
    # mon_list=mon_list.extra(select = {'list_type': 0})
    # mon_list=mon_list.extra(select = {'list_description': ''})
    # mon_list=mon_list.extra(select = {'porsantaj_ratio': 0})
    # mon_list=mon_list.extra(select = {'hard_ratio': 0})

    
    mon=mon_list.values_list('workhouse__Code','workhouse__Name','workhouse__Client','workhouse__Address','list_type',
                'year','month','list_number','list_description','worker_num','days_sum','daily_wage_sum','monthly_wage_sum','monthly_advantage',
                'monthly_wage_and_advantage','total_wage','insured_share_sum','employer_share_sum','unemployment_premium_sum',
                'workhouse__Ratio','porsantaj_ratio','hard_ratio','workhouse__ContractRow',  )

    for m in mon:
        m=list(m)
        m[1]=reverse(m[1])
        m[2]=reverse(m[2])
        m[3]=reverse(m[3])
        m[8]=reverse(m[8])


        writer.writerow(m)   

    
            
    return response



def export_workers_data(request): 

    #this section for .csv files

    response = HttpResponse(content_type='text/csv ;charset=iransystem')
    response['Content-Disposition'] = 'attachment;  filename="work_list.txt"'

    writer = csv.writer(response)
    # writer.writerow(['header names list'])
    workers_list=DetailsList.objects.all()


    workers_list=workers_list.annotate(monthly_wage=(ExpressionWrapper(F('working_days') * F('daily_wage') , output_field=BigIntegerField())))
    workers_list=workers_list.annotate(monthly_wage_and_advantage=(ExpressionWrapper( F('advantage') + (F('daily_wage') * F('working_days')), output_field=BigIntegerField()) )) 
    workers_list=workers_list.annotate(total_wage=(ExpressionWrapper( F('advantage') + (F('daily_wage') * F('working_days')), output_field=BigIntegerField()) )) 
    workers_list=workers_list.annotate(insured_share=ExpressionWrapper(F('total_wage')*.07,output_field=BigIntegerField()  ))
    workers_list=workers_list.annotate(list_number=Value('01', CharField()))
    workers_list=workers_list.annotate(porsantaj_ratio=Value('0', CharField()))
    
   
   
    # workers = workers_list.values_list('month_list__workhouse__Code','month_list__year',
    #                     'month_list__month','list_number','worker__BimehNum','worker__FirstName','worker__LastName',
    #                     'worker__DadName','worker__IdNum','worker__IdPlace','worker__RegisterDate',
    #                     'worker__BirthDate','worker__Sex','worker__Nationality','worker__Job',
    #                     'start_date','end_date','working_days','daily_wage','monthly_wage',
    #                     'advantage','monthly_wage_and_advantage','total_wage','insured_share','porsantaj_ratio',
    #                     'worker__Job','worker__NationNum',)

    #new stracture
    workers = workers_list.values_list('month_list__workhouse__Code','month_list__year',
                        'month_list__month','list_number','worker__BimehNum','worker__FirstName','worker__LastName',
                        'worker__DadName','worker__IdNum','worker__IdPlace','worker__RegisterDate',
                        'worker__Sex','worker__Nationality','worker__Job',
                        'start_date','end_date','working_days','daily_wage','monthly_wage',
                        'advantage','monthly_wage_and_advantage','total_wage','insured_share','porsantaj_ratio',
                        'worker__Job','worker__BirthDate','worker__NationNum',)


    #TODO:advantage is daily or note
    #TODO : diffrence between monthly_wage_and_advantage and total_wage

    sex_chioce_dict={'1':'مرد','2':'زن'}
    job_chioce_dict={code:value for code,value in job_choice}
    nat_chioce_dict={'1':'ايراني','2':'غیر ايراني'}
    city_chioce_dict={code:value for code,value in city_choice}
    for worker in workers:
        worker=list(worker)

        worker[5]=reverse(worker[5])
        worker[6]=reverse(worker[6])
        worker[7]=reverse(worker[7])

        #remove two zero at insuranse code
        worker[4]=worker[4][2:]

        #define sex describ instead of its code
        worker[11]=reverse(sex_chioce_dict[worker[11]]) 

        #define job describ instead of its code
        worker[13]=reverse(job_chioce_dict[worker[13]])

        #define nationality describ instead of its code
        worker[12]=reverse(nat_chioce_dict[worker[12]])

        #define city describ instead of its code
        worker[9]=reverse(city_chioce_dict[worker[9]])
  
        writer.writerow(worker)
    return response


#########################################
    # with open('w.txt', 'w', newline='', encoding='iransystem') as f:
    #     writer = csv.writer(f)
    #     for worker in workers:

                

    #         worker=list(worker)
            
  
    #         #remove two zero at insuranse code
    #         worker[4]=worker[4][2:]

    #         #define sex describ instead of its code
    #         worker[11]=sex_chioce_dict[worker[11]]

    #         #define job describ instead of its code
    #         worker[13]=job_chioce_dict[worker[13]]

    #         #define nationality describ instead of its code
    #         worker[12]=nat_chioce_dict[worker[12]]

    #         #define city describ instead of its code
    #         worker[9]=city_chioce_dict[worker[9]]

    #         w=[]
            
    #         writer.writerow(worker)  


    #         # for i in worker:
    #         #     i=str(i)
    #         #     # i=i.encode('utf-8')
    #         #     # i=i.decode('iransystem')
    #         #     w.append(i)
    #         # worker=w
    #         # writer.writerow(worker)  
    # return response
######################################


def import_workhouses_data(request):
    
    # importing csv module 
    import csv 

    # csv file name 
    filename = "workhouse.csv"

    # initializing the titles and rows list 
    # fields = [] 
    rows = [] 

    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        # fields = csvreader.next() 

        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
            obj=WorkHouse(Code=row[1],ContractRow=row[2],Name=row[3],Client=row[4],Address=row[5],Ratio=row[6])
            obj.save()
    
    return HttpResponse('done')


def import_workers_data(request):

    # importing csv module 
    import csv 

    # csv file name 
    filename = "workers.csv"

    # initializing the titles and rows list 
    # fields = [] 
    rows = [] 

    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        # fields = csvreader.next() 

        # extracting each data row one by one 
    
        for row in  csvreader:

            # covreting city_name to city_code
            c=[x for x, y in city_choice if y == row[8]]
            if c != []:
                row[8]=c[0]
                row[9]=c[0]
                
            # row[10]=row[10].split('/')
            # row[10]=''.join(row[10])
            row[10]=row[10][2:]

            # row[11]=row[11].split('/')
            # row[11]=''.join(row[11])
            row[11]=row[11][2:]
            
            rows.append(row) 

            obj=Workers(BimehNum=row[1],PersoneliNum=row[2],LastName=row[3],FirstName=row[4],DadName=row[5],NationNum=row[6],
                        IdNum=row[7],IdPlace=row[8],BirthPlace=row[9],BirthDate=row[10],RegisterDate=row[11],Sex=row[12],
                        Nationality=row[15],Job=row[21],)
            obj.save()

        #TODO IdPlace=,BirthPlace=, most some consultations and BirthDate=,RegisterDate=

    return HttpResponse('done')


def workhouse_reg(request):
    if request.method== 'POST':

        workhouse_form=WorkhouseForm(request.POST)
        if workhouse_form.is_valid():
            workhouse_form.save()
            return  HttpResponseRedirect('/main/workhouses_list/')
            # return HttpResponseRedirect(reverse('main:workhouses_list'))
        else:
            return HttpResponse('not valid')
    else:        
        workhouse_form=WorkhouseForm()
        context={
            'workhouse_form':workhouse_form
        }

    return render(request,'main/workhouse_reg.html',context)
   
   
def workers_reg(request):
    if request.method== 'POST':
        workers_form=WorkersForm(request.POST)
        if workers_form.is_valid():
            workers_form.save()
            return  HttpResponseRedirect('/main/workers_list/')
        else:
            return HttpResponse('not valid')
    else:        
    

        workers_form=WorkersForm()

        context={
            'workers_form':workers_form
        }

    return render(request,'main/workers_reg.html',context)

def list_reg(request):
    monthlist_form=MonthlistForm()

    context={
        'monthlist_form':monthlist_form
        }

    return render(request,'main/monthlist_form.html',context)


def details_reg(request):
    details_form=DetailsForm()

    context={
        'details_form':details_form
        }

    return render(request,'main/details_form.html',context)