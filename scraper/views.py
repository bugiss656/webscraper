from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

from scraper.models import PopularCurrencyModel, AllCurrencyModel

def indexView(request):
    return render(request, 'homepage/homepage.html')

def popularCurrencyView(request):

    url = 'https://kursy-walut.mybank.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.find('div', class_= 'cen')
    box = content.find_all('b')

    delete_query = PopularCurrencyModel.objects.all().delete()

    namePattern = box[0::3]
    ratePattern = box[1::3]
    changePattern = box[2::3]

    popularCurrencyNames = [i.text for i in namePattern]
    popularCurrencyRates = [i.text for i in ratePattern]
    popularCurrencyChanges = [i.text for i in changePattern]

    popularCurrencyData = [
        PopularCurrencyModel(
            name=popularCurrencyNames[i],
            rate=popularCurrencyRates[i],
            change=popularCurrencyChanges[i]
        )
        for i in range(len(namePattern))
    ]

    add_query = PopularCurrencyModel.objects.bulk_create(popularCurrencyData)

    context = {
        'names': popularCurrencyNames,
        'rates': popularCurrencyRates,
        'changes': popularCurrencyChanges,
        'data': popularCurrencyData
    }

    return render(request, 'popularCurrency/popular-currency.html', context)

def allCurrencyView(request):

    url = 'https://kursy-walut.mybank.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', class_='tab_kursy')
    row = table.find_all('td')

    delete_query = AllCurrencyModel.objects.all().delete()

    namePattern = row[0::5]
    symbolPattern = row[1::5]
    ratePattern = row[2::5]
    changePattern = row[3::5]

    allCurrencyNames = [i.text for i in namePattern]
    allCurrencySymbols = [i.text for i in symbolPattern]
    allCurrencyRates = [i.text for i in ratePattern]
    allCurrencyChanges = [i.text for i in changePattern]

    allCurrencyData = [
        AllCurrencyModel(
            name=allCurrencyNames[i],
            symbol=allCurrencySymbols[i],
            rate=allCurrencyRates[i],
            change=allCurrencyChanges[i]
        )
        for i in range(len(namePattern))
    ]

    add_query = AllCurrencyModel.objects.bulk_create(allCurrencyData)

    context = {
        'names': allCurrencyNames,
        'symbols': allCurrencySymbols,
        'rates': allCurrencyRates,
        'changes': allCurrencyChanges,
        'data': allCurrencyData
    }

    return render(request, 'allCurrency/all-currency.html', context) 

def aboutView(request):
    return render(request, 'about/about.html')
