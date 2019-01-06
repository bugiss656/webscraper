from django.contrib import admin
from .models import PopularCurrencyModel, AllCurrencyModel

admin.site.register(PopularCurrencyModel)
admin.site.register(AllCurrencyModel)