# Generated by Django 3.0.3 on 2020-04-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200330_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='Job',
            field=models.CharField(choices=[('024032', 'کارگرساده'), ('2', 'مهندس')], max_length=10, verbose_name='شغل'),
        ),
    ]
