from django.shortcuts import render
from django.http import HttpResponse
from scraper.classModule import *

def indexView(request):
    return render(request, 'homepage/homepage.html')

def popularCurrencyView(request):

    popularCurrencyObject = popularCurrency()
    popularCurrencyObject.clearData()
    popularCurrencyObject.scrapPopularCurrency()

    context = {
        'currencyNames': popularCurrencyObject.popularCurrencyNames,
        'currencyRates': popularCurrencyObject.popularCurrencyRates,
        'currencyChanges': popularCurrencyObject.popularCurrencyChanges,
        'dataObject': popularCurrencyObject.popularCurrencyData
    }

    return render(request, 'popularCurrency/popular-currency.html', context)

def allCurrencyView(request):
    return render(request, 'allCurrency/all-currency.html') 

def aboutView(request):
    return render(request, 'about/about.html')
