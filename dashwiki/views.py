import collections
from itertools import product
from pickle import NONE
from django.shortcuts import render, redirect
from .models import DashboardCollection, DashboardPage

def list_dashcollections(request):
    dashcollection = DashboardCollection.objects.all()
    return render(request, 'dashcollections.html', {'dashcollection': dashcollection})

def list_dashpages(request):
    dashpages = DashboardPage.objects.all()
    return render(request, 'dashpages.html', {'dashpages': dashpages})

def list_dashpages_by_collection(request, id):
    dashpages_by_collection = DashboardPage.objects.all().filter(collection=id)
    return render(request, 'dashpages_by_collection.html', {'dashpages_by_collection': dashpages_by_collection})