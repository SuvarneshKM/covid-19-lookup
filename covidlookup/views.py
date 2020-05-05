from django.shortcuts import render
from django.shortcuts import render, redirect

def home(request):
	return render(request, 'home.html', {})            

def covidlookup(request):
	import requests

	import json

	covid_request = requests.get("https://api.covid19api.com/summary")
	covid = covid_request.json()["Countries"]
	# covid = json.loads(covid_request.content)

	return render(request, 'covidlookup.html', {'covid': covid})

def covidlookup_india(request):
	# import requests

	# import json

	# covid_request_ind = requests.get("https://covid-india-api.herokuapp.com/api")
	# covid_ind = covid_request_ind.json()["data"]
	# #covid = json.loads(covid_request.content)

	return render(request, 'covidlookup_india.html', {})

