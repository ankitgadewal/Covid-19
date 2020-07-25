from django.shortcuts import render, HttpResponse
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

# testing api resonse with jwt token
def apis(request):
    students_data = requests.get('http://ankitrestapi.pythonanywhere.com/students', headers={'Authorization': 'Bearer {token}'.format(token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk1NjgwNDEwLCJqdGkiOiIwN2NlZjFkNzUwNDI0Yzk5ODJjM2U5MWIwYTcxN2E3NyIsInVzZXJfaWQiOjV9.HWF6IF6EG7oe1u7_Y9_YW7X0lrg6ZoLNmV44yRM-D_U')})
    students_data = students_data.json()
    print(students_data)
    return HttpResponse(f'{students_data}')

def postapis(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        myobj = {'username': username, 'password': password}
        gettoken = requests.post('http://ankitrestapi.pythonanywhere.com/api/token/', data=myobj)
        newdata = gettoken.text
        newdict = json.loads(newdata)
        newvalue = (newdict['access'])
        return render(request, 'login.html', {'newvalue':newvalue})
    else:
        return render(request, 'login.html')