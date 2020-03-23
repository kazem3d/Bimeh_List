from django.urls import path
from main import views

app_name ='main'
urlpatterns=[
  
    path('workers_list/',views.workers_list,name="workers_list"),
    path('workhouses_list/',views.workhouses_list,name="workhouses_list")

]