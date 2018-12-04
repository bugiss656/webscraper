from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('popular-currency/', views.popularCurrency, name="popular-currency"),
    path('all-currency/', views.allCurrency, name="all-currency"),
    path('about/', views.about, name="about")
]