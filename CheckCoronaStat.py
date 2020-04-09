#made by Kerszi 08.04.2020
#CheckCoronaStat
from urllib.request import urlopen
from urllib.error import URLError
import json
import sys

LINK='https://coronavirus-19-api.herokuapp.com/countries/'
BLEDY_POLACZENIA={"[Errno 11001] getaddrinfo failed":"Nie moge wczytaj strony"}
BLEDY_JSON={"Country not found":"Nie ma takiego kraju:"}
WSZYSTKIE_KRAJE_PARAM=["kraje"]
WSZYSTKIE_KRAJE=["Sprobuj: CheckCoronaStat"]




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


def wyswietl_kraje ():
    BODY=polacz_sie(LINK)
    WSZYSTKIE_KRAJE_NAZWA=json.loads(BODY)
    POSORTOWANE_KRAJE=[]
    for i in WSZYSTKIE_KRAJE_NAZWA:
        POSORTOWANE_KRAJE.append(i['country'])    
    len_POSORTOWANE_KRAJE=len(POSORTOWANE_KRAJE)
    for counter,i in enumerate(sorted(POSORTOWANE_KRAJE)):         
        if counter>0 and counter<len_POSORTOWANE_KRAJE-1:
            print (i+", ",end='')
        if counter==len_POSORTOWANE_KRAJE-1:
            print (i+" ",end='')



def sprawdz_ilosc_parametrow():
    PARAMETRY=[]
    total = len(sys.argv)
    cmdargs = sys.argv

    if total==1:
        PARAMETRY=["World"]
        return PARAMETRY        
    if total==2 and WSZYSTKIE_KRAJE_PARAM[0]==cmdargs[1]:        
            wyswietl_kraje ()
            exit()
    PARAMETRY=cmdargs[1:]
    return PARAMETRY



def polacz_sie(_link):
    try:
        _HTML_BODY=urlopen(_link)
    except URLError as e:        
        print (BLEDY_POLACZENIA[str(e.reason)])
        exit()
    else:        
        HTML_BODY=_HTML_BODY.read()        
        if "Country not found" in str(HTML_BODY):
            print(BLEDY_JSON["Country not found"]+" "+_link.split('/')[-1])
            print(WSZYSTKIE_KRAJE[0]+" "+WSZYSTKIE_KRAJE_PARAM[0])
            exit()
        else:
            return HTML_BODY


def json_dekoduj(_body):
    #try:
    JSON_DECODE=json.loads(_body)
    #except ValueError as e:
        #NIE_MA_KRAJU=_body.decode()
        #print (BLEDY[NIE_MA_KRAJU])
        #exit()
    #else:        
    JSON_DECODE_TRANS={}
    for i in JSON_DECODE:        
        JSON_DECODE_TRANS[AngielskieSlowa[i]]=JSON_DECODE[i]
    return JSON_DECODE_TRANS


def dodaj_kraje_do_tablicy(KTORE_KRAJE):        
    kraje={}
    for i in KTORE_KRAJE:
        kraj=i
        HTML_BODY=polacz_sie(LINK+kraj)
        JSON_DECODE_TRANS=json_dekoduj(HTML_BODY)
        kraje[i]=JSON_DECODE_TRANS
    return kraje


def wypisz_kraje(kraje):
    for i in AngielskieSlowa.values():
        print (f"{i:25} ",end='')
        for j in kraje:
            print (f"{kraje[j][i]:<10}",end='')
        print ("")


#wyswietl_kraje()

KTORE_KRAJE=sprawdz_ilosc_parametrow()
kraje=dodaj_kraje_do_tablicy(KTORE_KRAJE)
wypisz_kraje(kraje)


