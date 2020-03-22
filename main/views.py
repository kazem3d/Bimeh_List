from django.shortcuts import render

def home(request):
    return render(request,"main/home.html")


def workers_list(request):
    return render(request,"main/workers_list.html")

