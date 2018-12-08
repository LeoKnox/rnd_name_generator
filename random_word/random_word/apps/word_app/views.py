from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    request.session['str']=''
    request.session['counter']=0
    return render(request, "word_app/index.html")


def random_word(request):
    request.session['str']=get_random_string(length=14)
    request.session['counter']+=1
    return render(request, "word_app/index.html")
# Create your views here.
