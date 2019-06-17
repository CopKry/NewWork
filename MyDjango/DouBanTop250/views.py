from django.shortcuts import render
from DouBanTop250.models import douban

def douban_dir(request):
    rows=douban.objects.all()
    return render(request,'Top250.html',{'content':rows})

def index_dir(request):
    return render(request,'Index.html')
