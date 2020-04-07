from urllib.request import urlopen
from urllib.error import URLError
import json
import sys

BLEDY={"[Errno 11001] getaddrinfo failed":"Nie moge wczytaj strony",
        "Country not found":"Nie ma takiego kraju"}

LINK='https://coronavirus-19-api.herokuapp.com/countries/'


AngielskieSlowa={"country":"Panstwo:",
                 "testsPerOneMillion":"Testy na milion:",
                 "todayCases":"Dzisiejsze przypadki:",
                 "totalTests":"Liczba wszystkich testow:",
                 "todayDeaths":"Dzisiejsze zgony:",
                 "deathsPerOneMillion":"Zgony na milion:",
                 "cases":"Wszystkie przypadki:",
                 "active":"Aktywne przypadki:",
                 "deaths":"Zgony:",
                 "casesPerOneMillion":"Przypadki na milion:",
                 "recovered":"Wyleczeni:",
                 "critical":"W stanie krytycznym:"
                 }

#PARAMETRY=["World","ddf"]
#total = len(sys.argv)
 
# Get the arguments list 
#cmdargs = str(sys.argv)
#print (cmdargs)

if total==1:
    PARAMETRY=

"""
def polacz_sie(_link):
    try:
        _HTML_BODY=urlopen(_link)
    except URLError as e:        
        print (BLEDY[str(e.reason)])
        exit()
    else:
        HTML_BODY=_HTML_BODY.read()
        return HTML_BODY
   


def json_dekoduj(_body):
    try:
        JSON_DECODE=json.loads(_body)
    except ValueError as e:
        NIE_MA_KRAJU=HTML_BODY.decode()
        print (BLEDY[NIE_MA_KRAJU])
        exit()
    else:        
        JSON_DECODE_TRANS={}
        for i in JSON_DECODE:        
            JSON_DECODE_TRANS[AngielskieSlowa[i]]=JSON_DECODE[i]
        return JSON_DECODE_TRANS



def WYPISZ_DANE(dane):
    dl=len(max(dane.keys(),key=len))
    for i in dane:
        print (f"{i:25} {dane[i]}")

kraje={}
kraj="poland"
HTML_BODY=polacz_sie(LINK+kraj)
JSON_DECODE_TRANS=json_dekoduj(HTML_BODY)
kraje["poland"]=JSON_DECODE_TRANS

kraj="sweden"
HTML_BODY=polacz_sie(LINK+kraj)
JSON_DECODE_TRANS=json_dekoduj(HTML_BODY)
kraje["sweden"]=JSON_DECODE_TRANS

for i in AngielskieSlowa.values():
    print (f"{i:25} ",end='')
    for j in kraje:
        print (f"{kraje[j][i]:<10}",end='')
    print ("")

"""