from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('scrape/', views.scrape_url, name='scrape_url'),
     path('extract-pdf/', views.extract_pdf, name='extract_pdf'),

]