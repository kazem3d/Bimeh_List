# Generated by Django 3.0.4 on 2020-03-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200322_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='Job',
            field=models.CharField(choices=[('1', 'کارگرساده'), ('2', 'مهندس')], max_length=10, verbose_name='شغل'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='Nationality',
            field=models.CharField(choices=[('1', 'ایرانی'), ('2', 'غیر ایرانی')], max_length=10, verbose_name='ملیت '),
        ),
        migrations.AlterField(
            model_name='workers',
            name='Sex',
            field=models.CharField(choices=[('1', 'مرد'), ('2', 'زن')], max_length=10, verbose_name='جنسیت '),
        ),
        migrations.CreateModel(
            name='MonthList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.WorkHouse', verbose_name='کارگاه ')),
            ],
        ),
    ]
