from django.shortcuts import render
import json
import requests

# Create your views here.
def apicall(request):
  appid="185a5b60b5b86a369f84a06359abb723"
  city='varanasi'
  status=''
  result=''
  if request.GET:
    city=request.GET['city']
  paramtr={'aapid':appid,'q':city,'units':'metric'}  
  url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
  response=requests.get(url,paramtr)
  code=response.status_code
  print(code)
  if code !=200:
    status="error"
    # return render(request,'weather.html',{"city":city,"result":"error"})
  else:
    result=json.loads(response.text)
  return render(request,'weather.html',{"city":city,"result":result,"status":status})
