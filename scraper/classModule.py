import requests
from bs4 import BeautifulSoup

class ScrapingOptions(object):
    
    url = 'https://kursy-walut.mybank.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


class popularCurrency(ScrapingOptions):

    popularCurrencyNames = []
    popularCurrencyRates = []
    popularCurrencyChanges = []
    popularCurrencyData = []

    def scrapPopularCurrency(self):
        content = self.soup.find('div', class_= 'cen')
        box = content.find_all('b')

        namePattern = box[0::3]
        ratePattern = box[1::3]
        changePattern = box[2::3]

        self.popularCurrencyNames = [i.text for i in namePattern]
        self.popularCurrencyRates = [i.text for i in ratePattern]
        self.popularCurrencyChanges = [i.text for i in changePattern]

        self.popularCurrencyData = [{
            'name': self.popularCurrencyNames[i],
            'rate': self.popularCurrencyRates[i],
            'change': self.popularCurrencyChanges[i]
        } for i in range(len(namePattern))]

        return self.popularCurrencyData

    def clearData(self):
        self.popularCurrencyNames.clear()
        self.popularCurrencyRates.clear()
        self.popularCurrencyChanges.clear()
        self.popularCurrencyData.clear()

        return self.popularCurrencyData


class allCurrency(ScrapingOptions):

    allCurrencyNames = []
    allCurrencyRates = []
    allCurrencyChanges = []
    allCurrencyData = []

    def scrapAllCurrency(self):
        table = self.soup.find('table', class_='tab_kursy')
        row = table.find_all('td')

        namePattern = row[0::5]
        ratePattern = row[2::5]
        changePattern = row[3::5]

        self.allCurrencyNames = [i.text for i in namePattern]
        self.allCurrencyRates = [i.text for i in ratePattern]
        self.allCurrencyChanges = [i.text for i in changePattern]

        self.allCurrencyData = [{
            'name': self.allCurrencyNames[i],
            'rate': self.allCurrencyRates[i],
            'change': self.allCurrencyChanges[i]
        } for i in range(len(namePattern))]

        return self.allCurrencyData

    def clearData(self):
        self.allCurrencyNames.clear()
        self.allCurrencyRates.clear()
        self.allCurrencyChanges.clear()
        self.allCurrencyData.clear()

        return self.allCurrencyData