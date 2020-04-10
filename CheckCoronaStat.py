#made by Kerszi 08.04.2020
#CheckCoronaStat
from urllib.request import urlopen
from urllib.error import URLError
from  datetime import datetime
import json
import sys
import re


LINK='https://coronavirus-19-api.herokuapp.com/countries/'
BLEDY_POLACZENIA={"[Errno 11001] getaddrinfo failed":"Nie moge wczytaj strony"}
BLEDY_JSON={"Country not found":"Nie ma takiego kraju:"}
WSZYSTKIE_KRAJE_PARAM=["kraje"]
WSZYSTKIE_KRAJE=["Sprobuj: CheckCoronaStat"]



PL_EN={}
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



def wyswietl_wszystkie_kraje_swiata ():
    BODY=polacz_sie(LINK)
    WSZYSTKIE_KRAJE_NAZWA=json.loads(BODY)
    POSORTOWANE_KRAJE=[]
    for i in WSZYSTKIE_KRAJE_NAZWA:
        POSORTOWANE_KRAJE.append(i['country'])    
    len_POSORTOWANE_KRAJE=len(POSORTOWANE_KRAJE)
    for counter,i in enumerate(sorted(POSORTOWANE_KRAJE)):         
        if counter>0 and counter<len_POSORTOWANE_KRAJE-1:
            if i!="Total:":
                i=i.replace(" ","%20")
                print (i+", ",end='')
        if counter==len_POSORTOWANE_KRAJE-1:
            print (i+" ",end='')
    return sorted(POSORTOWANE_KRAJE)



def sprawdz_ilosc_parametrow():
    PARAMETRY=[]
    total = len(sys.argv)
    cmdargs = sys.argv

    if total==1:
        PARAMETRY=["World"]
        return PARAMETRY        
    if total==2 and WSZYSTKIE_KRAJE_PARAM[0]==cmdargs[1]:        
            wyswietl_wszystkie_kraje_swiata ()
            exit()
    PARAMETRY=cmdargs[1:]
    for counter,i in enumerate(PARAMETRY):
        PARAMETRY[counter]=i.capitalize()
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


def dodaj_kraje_do_tablicy(WYBRANE_KRAJE):        
    kraje={}
    for i in WYBRANE_KRAJE:
        kraj=i
        HTML_BODY=polacz_sie(LINK+kraj)
        JSON_DECODE_TRANS=json_dekoduj(HTML_BODY)
        kraje[i]=JSON_DECODE_TRANS
    return kraje


def wypisz_kraje(kraje):
    for i in AngielskieSlowa.values():
        print (f"{i:25} ",end='')
        for j in kraje:
            if kraje[j][i]==j:
                print (f"{PL_EN[j]:<10}",end='')
            else:
                print (f"{kraje[j][i]:<10}",end='')
        print ("")

def wypisz_date ():
    czas=datetime.now()    
    print (f"{'Stan na:':<25} {czas}")

def zaladuj_nazwy_krajow():
    PL_EN_={}
    with open('kraje.json', 'r') as f:
        PL_EN_=json.load(f)
    return PL_EN_






"""
def PRZETLUMACZ_EN2PL (WYBRANE_KRAJE_):
    moj_url='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=pl&dt=t&q=$'
    for question in WYBRANE_KRAJE_:        
        przetlumaczone=urlopen(moj_url+question)
        HTML_BODY=przetlumaczone.read()
        #print (HTML_BODY)
        wynik=re.search(' [a-zA-Z ]*',str(HTML_BODY))
        wynik=wynik[0].strip()
        PL_EN[question.capitalize()]=wynik.capitalize()
        sleep(2)
"""        



WYBRANE_KRAJE=sprawdz_ilosc_parametrow()
#PRZETLUMACZ_EN2PL (WYBRANE_KRAJE)
PL_EN=zaladuj_nazwy_krajow()
kraje=dodaj_kraje_do_tablicy(WYBRANE_KRAJE)
wypisz_kraje(kraje)
wypisz_date()


#print (PL_EN)
#print (WSZYSTKIE_KRAJE_NAZWA)
#WSZYSTKIE_KRAJE_NAZWA.remove('')
#WSZYSTKIE_KRAJE_NAZWA_z=list(dict.fromkeys(WSZYSTKIE_KRAJE_NAZWA))
#WSZYSTKIE_KRAJE_NAZWA_z.remove('Total:')
#WSZYSTKIE_KRAJE_NAZWA_z2=[]
#for i in WSZYSTKIE_KRAJE_NAZWA_z:
#    print (i)
#    a=str(i).replace(" ","%20")
#    WSZYSTKIE_KRAJE_NAZWA_z2.append(a)    
#print (WSZYSTKIE_KRAJE_NAZWA_z[0])
#PRZETLUMACZ_EN2PL(WSZYSTKIE_KRAJE_NAZWA_z2[1:])
#PRZETLUMACZ_EN2PL(PL_EN)
#print (type(WSZYSTKIE_KRAJE_NAZWA_z))
#for i in WSZYSTKIE_KRAJE_NAZWA_z:
#    print (i)
#print (PL_EN)
#print (WSZYSTKIE_KRAJE_NAZWA)
#with open('kraje.json', 'w') as f:
    #json.dump(PL_EN, f, ensure_ascii=False)


    
    
"""
with open('polskie.txt', 'r') as f:
    polskie = f.read().splitlines()

for licz,i in enumerate(angielskie):
    slownik[i]=polskie[licz]

with open('kraje.json', 'w') as f:
    json.dump(slownik, f, ensure_ascii=False)
"""
"""
"""

"""
question="norway"
#question="North%20Macedonia"
#moj_url='https://translate.googleapis.com/translate_a/single?client=gtx&sl=pl&tl=en&dt=t&q=${question}'
#moj_url='https://translate.googleapis.com/translate_a/single?client=gtx&sl=pl&tl=en&dt=t&q=$Norwegia'



przetlumaczone=urlopen(moj_url+question)
HTML_BODY=przetlumaczone.read()
#print (HTML_BODY)

#wynik=re.search(' [a-zA-Z ]*',str(HTML_BODY))
#print (re.sub('\[\[\[\"\$ ','',str(HTML_BODY)))

#print (wynik[0].strip())
"""
