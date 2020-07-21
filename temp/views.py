from django.shortcuts import render
import requests
import json
def index(request):
    worldwide = requests.get("https://api.covid19api.com/summary")
    indore_data = requests.get('https://api.covid19india.org/state_district_wise.json')

    #world_wide data
    worldwide_data = worldwide.json()
    def myFunc(e):
        return e['TotalConfirmed']
    countries = worldwide_data['Countries']
    countries.sort(reverse=True, key=myFunc)
    overall = worldwide_data['Global']


    #state wise data
    indore_data = indore_data.json()
    indore = indore_data['Madhya Pradesh']['districtData']['Indore']
    # print(data['Countries'][23]['TotalDeaths'])

    # url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    # headers = {
    #     'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    #     'x-rapidapi-key': "57ce057c1bmsh10bb653480a194ap1de136jsnc93f195df1ac"
    #     }

    # response = requests.request("GET", url, headers=headers)
    # response = response.json()

    # print(response['countries_stat'][0]['total_tests'])
    return render(request, 'index.html', {'countries': countries, 'overall': overall, 'indore': indore})
