from django.urls import path
from main import views

app_name ='main'
urlpatterns=[
  
    path('workers_list/',views.workers_list,name="workers_list"),
    path('workhouses_list/',views.workhouses_list,name="workhouses_list"),
    path('month_list/',views.month_list,name="month_list"),
    path('details_list/<int:list_id>',views.details_list,name="details_list"),
    path('export_kar/',views.export_workhouse_data, name='export_workhouse_data'),
    path('export_worker/',views.export_workers_data, name='export_workers_data'),
    path('import_workhouses/',views.import_workhouses_data, name='import_workhouses_data'),
    path('import_workers/',views.import_workers_data, name='import_workers_data'),
    path('workhouse_reg/',views.workhouse_reg, name='workhouse_reg'),
    path('workers_reg/',views.workers_reg, name='workers_reg'),
    path('list_reg/',views.list_reg, name='list_reg'),
    path('details_reg/',views.details_reg, name='details_reg'),




]