import requests
from bs4 import BeautifulSoup

class ScrapingOptions:
    url = 'https://kursy-walut.mybank.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


class popularCurrency(ScrapingOptions):
    
    def scrapPopularCurrency(self):
        content = self.soup.find('div', class_= 'cen')
        box = content.find_all('b')

        namePattern = box[0::3]
        ratePattern = box[1::3]
        changePattern = box[2::3]

        popularCurrencyNames = [i.text for i in namePattern]
        popularCurrencyRates = [i.text for i in ratePattern]
        popularCurrencyChanges = [i.text for i in changePattern]

        popularCurrencyData = [{
            'name': popularCurrencyNames[i],
            'rate': popularCurrencyRates[i],
            'change': popularCurrencyChanges[i]
        } for i in range(len(namePattern))]

        return popularCurrencyData


class allCurrency(ScrapingOptions):

    def scrapAllCurrency(self):
        table = self.soup.find('table', class_='tab_kursy')
        row = table.find_all('td')

        namePattern = row[0::5]
        ratePattern = row[2::5]
        changePattern = row[3::5]

        allCurrencyNames = [i.text for i in namePattern]
        allCurrencyRates = [i.text for i in ratePattern]
        allCurrencyChanges = [i.text for i in changePattern]

        allCurrencyData = [{
            'name': allCurrencyNames[i],
            'rate': allCurrencyRates[i],
            'change': allCurrencyChanges[i]
        } for i in range(len(namePattern))]

        return allCurrencyData



