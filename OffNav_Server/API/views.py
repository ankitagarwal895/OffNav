from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from requests.auth import HTTPBasicAuth
import requests
import json
import unicodedata
import re

SID="ACc28139bb6fc669e6a844f9b318945108"
AUTH_TOKEN="95f8576871d3b3dbc33fdcdbd6d09425"
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
    if(parsed_json["status"]=='OK'):
        limit=len(parsed_json["routes"][0]["legs"][0]["steps"])
        print limit
        if(limit<=15):
            start_add=str(parsed_json["routes"][0]["legs"][0]["start_address"])
            distance=int(parsed_json["routes"][0]["legs"][0]["distance"]["value"])
            distance="0."+start_add+'\%'+'%d'%(distance)
            data={"Body":distance,"From":"+1256801280","To":a}
            res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
            count=0
            for i in range(len(parsed_json["routes"][0]["legs"][0]["steps"])):
                final=str(parsed_json["routes"][0]["legs"][0]["steps"][i]["html_instructions"])
                final=final.replace("<b>","");
                final=final.replace("</b>","");
                final=final.replace("&nbsp;","");
                final = re.sub(r"</?div.*?>", "", final)
                #shortening message
                final=re.sub("head", "@H", final, flags=re.I)
                final=re.sub("north", "@N", final, flags=re.I)
                final=re.sub("towards", "@2", final, flags=re.I)
                final=re.sub("turn", "@T", final, flags=re.I)
                final=re.sub("left", "@L", final, flags=re.I)
                final=re.sub("onto", "@O", final, flags=re.I)
                final=re.sub("right", "@R", final, flags=re.I)
                final=re.sub("slight right", "@SR", final, flags=re.I)

                if(len(final)>100):
                    dist=str(parsed_json["routes"][0]["legs"][0]["steps"][i]['distance']['value'])
                    comp='%d.'%(count+1)+final[:100]+'%'+dist
                    data={"Body":comp,"From":"+1256801280","To":a}
                    res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
                    count+=1
                    dist=str(parsed_json["routes"][0]["legs"][0]["steps"][i]['distance']['value'])
                    comp='%d.'%(count+1)+final[100:]+'%'
                    data={"Body":comp,"From":"+1256801280","To":a}
                    res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
                else:
                    dist=str(parsed_json["routes"][0]["legs"][0]["steps"][i]['distance']['value'])
                    comp='%d.'%(count+1)+final+'%'+dist
                    data={"Body":comp,"From":"+1256801280","To":a}
                    res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
                count+=1
            return Response({"success":True})
        else:
            distance=int(parsed_json["routes"][0]["legs"][0]["distance"]["value"])
            distance="-1."
            data={"Body":distance,"From":"+1256801280","To":a}
            res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
            return Response({"error":-1})
    elif(parsed_json["status"]=='NOT_FOUND'):
        if(str(parsed_json["geocoded_waypoints"][0]["geocoder_status"])!="OK"):
            distance="-2."
            data={"Body":distance,"From":"+1256801280","To":a}
            res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
            return Response({"error":-2})
        elif(str(parsed_json["geocoded_waypoints"][1]["geocoder_status"])!="OK"):
            distance="-3."
            data={"Body":distance,"From":"+1256801280","To":a}
            res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
            return Response({"error":-3})
    else:
        distance="-4."
        data={"Body":distance,"From":"+1256801280","To":a}
        res=requests.post('https://api.twilio.com/2010-04-01/Accounts/'+SID+"/Messages.json", auth=HTTPBasicAuth(SID,AUTH_TOKEN),data=data)
        return Response({"error":-4})