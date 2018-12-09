from django.shortcuts import render, HttpResponse, redirect
from random import *

def index(request):
    if 'gold' in request.session:
        print('ok')
    else:
        request.session['gold']
    if 'activities' in request.session:
        print('ok')
    else:
        request.session['activities']

    return render(request, "goldapp/index.html")

def process_gold(request):
    
    if request.POST["imin"] == 'cave':
        x=randrange(5,11)
        request.session['gold'] += x
        request.session['activities']+="Went to cave and earned " + str(x) + " gold\n"
    if request.POST["imin"] == 'farm':
        x=randrange(10,21)
        request.session['gold'] += x
        request.session['activities']+="Went to cave and earned " + str(x) + " gold\n"
    if request.POST["imin"] == 'house':
        x=randrange(2,6)
        request.session['gold'] += x
        request.session['activities']+="Went to cave and earned " + str(x) + " gold\n"
    if request.POST["imin"] == 'casino':
        x=randrange(-50, 50)
        request.session['gold'] += x
        if x<0:
            request.session['activities']+="Went to casino and lost " + str(x) + " gold\n"
        else:
            request.session['activities']+="Went to casino and won " + str(x) + " gold\n"
    return redirect('/')

def dele(request):
    request.session['gold']=0
    request.session['activities']=""

    return redirect('/')

# Create your views here.
