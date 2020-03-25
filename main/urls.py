from django.urls import path
from main import views

app_name ='main'
urlpatterns=[
  
    path('workers_list/',views.workers_list,name="workers_list"),
    path('workhouses_list/',views.workhouses_list,name="workhouses_list"),
    path('month_list/',views.month_list,name="month_list"),
    path('details_list/<int:list_id>',views.details_list,name="details_list"),

]