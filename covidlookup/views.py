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
	import requests
	import json
	url = "https://covid19india.p.rapidapi.com/getIndiaStateData"

	headers = {
	    'x-rapidapi-host': "covid19india.p.rapidapi.com",
	    'x-rapidapi-key': "70accf0d7emsh6414b2c869b263ap1f6c58jsn1907c7802435"
		    }

	response = requests.request("GET", url, headers=headers)

		
	covid_ind = response.json()["response"]

	return render(request, 'covidlookup_india.html', {'covid_ind': covid_ind})

def covidlookup_kerala(request):
	import requests
	import json

	api_request = requests.get("https://api.covid19india.org/v2/state_district_wise.json")
	api = json.loads(api_request.content)
	state_code = ["KL"]

	for x in api:
	    for code in state_code:
	       if code == x["statecode"]:
	            api_kl = x["districtData"]

	            return render(request, 'covidlookup_kerala.html', {'api_kl': api_kl})
