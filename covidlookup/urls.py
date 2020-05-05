from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('covidlookup', views.covidlookup, name="covidlookup"),
	path('covidlookup_india', views.covidlookup_india, name="covidlookup_india"),
	path('covidlookup_kerala', views.covidlookup_kerala, name="covidlookup_kerala"),

]             