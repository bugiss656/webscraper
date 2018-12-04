from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')

def popularCurrency(request):
    return render(request, 'popularCurrency/popular-currency.html')

def allCurrency(request):
    return render(request, 'allCurrency/all-currency.html') 

def about(request):
    return render(request, 'about/about.html')
