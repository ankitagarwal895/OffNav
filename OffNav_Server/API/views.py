from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from requests.auth import HTTPBasicAuth
import requests
import json
import unicodedata
print unicodedata.normalize('NFKD', u"Turn \u003cb\u003eleft\u003c/b\u003e at \u003cb\u003eASC Jct\u003c/b\u003e onto \u003cb\u003eOld Airport Rd\u003c/b\u003e/\u003cb\u003eThyagi M Palanivelu Rd\u003c/b\u003e\u003cdiv \u003eContinue to follow Old Airport Rd\u003c/div\u003e\u003cdiv \u003ePass by Canara Bank ATM (on the left in 2.1&nbsp;km)\u003c/div\u003e\u003cdiv \u003eDestination will be on the left\u003c/div\u003e").encode('ascii','ignore')

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
    temp=b.split('%')
    url=urls[0]+temp[0]+urls[1]+temp[1]+urls[2]
    #print url
    res=requests.get(url)
    parsed_json=json.loads(res.text)
    distance=int(parsed_json["routes"][0]["legs"][0]["distance"]["value"])
    data={"Body":distance,"From":"+12513331811","To":a}
    res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
    for i in range(len(parsed_json["routes"][0]["legs"][0]["steps"])):
	    final=str(parsed_json["routes"][0]["legs"][0]["steps"][i]["html_instructions"])
	    final=final.replace("<b>","");
	    final=final.replace("</b>","");
	    data={"Body":final,"From":"+12513331811","To":a}
	    res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
    return Response({"success":True})