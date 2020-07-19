from django.shortcuts import render
import requests
import json
def index(request):
    response = requests.get("https://api.covid19api.com/summary")
    data = response.json()
    countries = data['Countries']
    overall = data['Global']
    # print(data['Countries'][23]['TotalDeaths'])
    return render(request, 'index.html', {'countries': countries, 'overall': overall})