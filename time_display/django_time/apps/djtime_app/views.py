from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    x = datetime.datetime.now()
    curtime = {
        "date": x.strftime("%c"),
    }
    return render(request, "djtime_app/index.html", curtime)