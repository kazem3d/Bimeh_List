# Generated by Django 3.0.4 on 2020-03-30 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200326_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailslist',
            name='end_date',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='تاریخ پایان به کار '),
        ),
        migrations.AddField(
            model_name='detailslist',
            name='start_date',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='تاریخ شروع به کار '),
        ),
        migrations.AddField(
            model_name='workers',
            name='BirthDate',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='تاریخ تولد '),
        ),
        migrations.AddField(
            model_name='workers',
            name='RegisterDate',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='تاریخ صدور '),
        ),
    ]
