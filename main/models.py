from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from main.choices import *

class WorkHouse(models.Model):

    class Meta:

        verbose_name=' ثبت کارگاه '
        verbose_name_plural=' ثبت کارگاه '


    Code=models.CharField('کد کارگاه',max_length=10,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])
    ContractRow=models.CharField('ردیف پیمان',max_length=3,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])
    Name=models.CharField('نام کارگاه',max_length=24)
    Client=models.CharField('نام کارفرما',max_length=30)
    Address=models.CharField('آدرس کارگاه',max_length=40)
    Ratio=models.CharField('نرخ حق بیمه',max_length=2,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])
    
    

    def __str__(self):
        return 'نام کارگاه :{}- کد کارگاه :{} - ردیف پیمان: {}'.format(self.Name,
                            self.Code,self.ContractRow)

class Workers(models.Model):

    class Meta:

        verbose_name='کارکنان'
        verbose_name_plural='کارکنان'

    BimehNum=models.CharField('شماره بیمه',max_length=10,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])

    PersoneliNum=models.CharField('شماره پرسنلی',max_length=10,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])

    LastName=models.CharField('نام خانوادگی',max_length=30)

    FirstName=models.CharField('نام ',max_length=30)

    DadName=models.CharField('نام پدر',max_length=30)

    NationNum=models.CharField('کد ملی ',max_length=10,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])
        
    IdNum=models.CharField('شماره شناسنامه',max_length=10,
                            validators=[RegexValidator(r'^\d{1,10}$',
                            message='فقط عدد وارد شود')])

    IdPlace=models.CharField('محل صدور ',choices=city_choice,max_length=10)

    BirthPlace=models.CharField('محل تولد ',choices=city_choice,max_length=10)

    Sex=models.CharField('جنسیت ',choices=sex_choice,max_length=10)

    Nationality=models.CharField('ملیت ',choices=nat_choice,max_length=10)

    Job=models.CharField('شغل',choices=job_choice,max_length=10)

    def __str__(self):
        return ' {} {} فرزند:{} شماره بیمه:{} شغل:{} '.format(self.FirstName ,
                    self.LastName,self.DadName,self.BimehNum,self.Job)


class MonthList(models.Model):

    class Meta:

        verbose_name='لیست ماهانه'
        verbose_name_plural='لیست ماهانه'

    
    workhouse=models.ForeignKey('WorkHouse',on_delete=models.CASCADE,verbose_name='کارگاه ')
    year=models.CharField('سال',max_length=2,null=True,
                                validators=[RegexValidator(r'^\d{1,10}$',
                                message='فقط عدد وارد شود')])
    month=models.CharField('ماه',max_length=2,null=True,
                                validators=[RegexValidator(r'^\d{1,10}$',
                                message='فقط عدد وارد شود')])

    def __str__(self):
        return 'لیست سال : {}  ماه :{} '.format(self.year,self.month)

class DetailsList(models.Model):

    
    class Meta:

        verbose_name=' جزئیات لیست '
        verbose_name_plural=' جزئیات لیست '

    month_list=models.ForeignKey('MonthList',on_delete=models.CASCADE,verbose_name='لیست ماهانه')
    worker=models.ForeignKey('Workers',on_delete=models.CASCADE,verbose_name=' نام کارگر')
    working_days=models.SmallIntegerField('تعداد روز کارکرد')
    daily_wage=models.BigIntegerField('دستمزد روزانه')
    advantage=models.BigIntegerField('مزایای ماهانه')

    def __str__(self):
        return '{} {} {} '.format(self.worker.FirstName,self.worker.LastName,self.month_list)
