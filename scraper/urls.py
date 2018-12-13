from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='homepage'),
    path('popular-currency/', views.popularCurrencyView, name="popular-currency"),
    path('all-currency/', views.allCurrencyView, name="all-currency"),
    path('about/', views.aboutView, name="about")
]