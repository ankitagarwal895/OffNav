from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from requests.auth import HTTPBasicAuth
import requests

SID="ACa38fdeeb011037900e62f2b1177ea6ec"
AUTH_TOKEN="6df2b92c807d6f48fa7aa1794a8b376a"
urls=[]
urls.append('https://maps.googleapis.com/maps/api/directions/json?origin=')
urls.append('&destination=')
urls.append('&key=AIzaSyBPfBImZ8ALTSY07YIwTNSd9g3tpx_foSc')

@api_view(['POST'])
def directions(request):
    a=request.data.get('From')
    b=request.data.get('Body')
    temp=b.split('&')
    url=urls[0]+temp[0]+urls[1]+temp[1]+urls[2]
    res=requests.get(url)
    data={"Body":b,"From":"+12513331811","To":a}
    #res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
    return Response(res)