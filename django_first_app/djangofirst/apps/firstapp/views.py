from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to display list of blogs...")


# Create your views here.
def new(request):
    return HttpResponse("placehold to form for creating blog ...")

def create(request):
    return redirect('/')

def show(request, my_val):
    return HttpResponse("display blog number: {}".format(my_val))

def edit(request, my_val):
    return HttpResponse("placeholder to edit blog {}".format(my_val))

def destroy(request, my_val):
    return redirect('/')