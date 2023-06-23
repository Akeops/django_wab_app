from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.today()
    return render(request, "merchex/listeBand.html", context = {"date": date})

def aboutUs(request):
    return render(request, "merchex/aboutUs.html")