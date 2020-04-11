#!/usr/bin/python3
#made by Kerszi 08.04.2020
#python >=3.6 (bo fstringi)
#CheckCoronaStat
#https://github.com/kerszl/CheckCoronaStat

from urllib.request import urlopen
from urllib.error import URLError
from  datetime import datetime
import json
import sys
import re

#Niestety wszystko ma byc w jednym pliku, wiec
#kod json nie potrzebny. Zostawiam go jednak tu
"""
def zaladuj_nazwy_krajow():
    PL_EN_={}
    try:
        with open('kraje.json', 'r') as f:
            PL_EN_=json.load(f)            
    except:
        print ("Jakis problem z plikiem: kraje.json")
        exit()
    return PL_EN_
"""
PL_EN={'Africa': 'Afryka', 'Albania': 'Albania', 'Algeria': 'Algieria', 'Andorra': 'Andora', 'Angola': 'Angola', 'Anguilla': 'Anguilla', 'Antigua%20and%20Barbuda': 'Antigua i Barbuda', 'Argentina': 'Argentyna', 'Armenia': 'Armenia', 'Aruba': 'Aruba', 'Asia': 'Azja', 'Australia': 'Australia', 'Austria': 'Austria', 'Azerbaijan': 'Azerbejdzan', 
'Bahamas': 'Bahamy', 'Bahrain': 'Bahrajn', 'Bangladesh': 'Bangladesz', 'Barbados': 'Barbados', 'Belarus': 'Bialorus', 'Belgium': 'Belgia', 'Belize': 'Belize', 'Benin': 'Benin', 'Bermuda': 'Bermudy', 'Bhutan': 'Bhutan', 'Bolivia': 'Boliwia', 'Bosnia%20and%20Herzegovina': 'Bosnia i Hercegowina', 'Botswana': 'Botswana', 'Brazil': 'Brazylia', 'British%20Virgin%20Islands': 'Brytyjskie Wyspy Dziewicze', 'Brunei': 'Brunei', 'Bulgaria': 'Bulgaria', 'Burkina%20Faso': 'Burkina Faso', 'Burundi': 'Burundi',
'Cabo%20Verde': 'Cabo Verde', 'Cambodia': 'Kambodza', 'Cameroon': 'Kamerun', 'Canada': 'Kanada', 'Caribbean%20Netherlands': 'Karaiby Holandia', 'Cayman%20Islands': 'Kajmany', 'Chad': 'Czad', 'Channel%20Islands': 'Wyspy Normandzkie', 'Chile': 'Chile', 'China': 'Chiny', 'Colombia': 'Kolumbia', 'Congo': 'Kongo', 'Costa%20Rica': 'Kostaryka', 'Croatia': 'Chorwacja', 'Cuba': 'Kuba', 'CuraĂ§ao': 'Curacao', 'Cyprus': 'Cypr', 'Czechia': 'Czechy',
'Denmark': 'Dania', 'Diamond%20Princess': 'Diamentowa ksiezniczka', 'Djibouti': 'Dzibuti', 'Dominica': 'Dominika', 'Dominican%20Republic': 'Republika Dominikany',
'Ecuador': 'Ekwador', 'Egypt': 'Egipt', 'El%20Salvador': 'Salwador', 'Equatorial%20Guinea':'Gwinea Rownikowa', 'Eritrea': 'Erytrea', 'Estonia': 'Estonia', 'Eswatini': 'Eswatini', 'Ethiopia': 'Etiopia', 'Europe': 'Europa', 
'Faeroe%20Islands': 'Wyspy Owcze', 'Falkland%20Islands': 'Falklandy', 'Fiji': 'Fidzi', 'Finland': 'Finlandia', 'France': 'Francja', 'French%20Guiana': 'Gujana Francuska', 'French%20Polynesia': 'Polinezja Francuska',
'Gabon': 'Gabon', 'Gambia': 'Gambia', 'Georgia': 'Gruzja', 'Germany': 'Niemcy', 'Ghana': 'Ghana', 'Gibraltar': 'Gibraltar', 'Greece': 'Grecja', 'Greenland': 'Grenlandia', 'Grenada': 'Grenada', 'Guadeloupe': 'Gwadelupa', 'Guatemala': 'Gwatemala', 'Guinea': 'Gwinea', 'Guinea-Bissau': 'Gwinea Bissau', 'Guyana': 'Gujana',
'Haiti': 'Haiti', 'Honduras': 'Honduras', 'Hong%20Kong': 'Hongkong', 'Hungary': 'Wegry', 
'Iceland': 'Islandia', 'India': 'Indie', 'Indonesia': 'Indonezja', 'Iran': 'Iran', 'Iraq': 'Irak', 'Ireland': 'Irlandia', 'Israel': 'Izrael', 'Italy': 'Wlochy', 'Ivory%20Coast': 'Wybrzeze Kosci Sloniowej', 
'Jamaica': 'Jamajka', 'Japan': 'Japonia', 'Jordan': 'Jordania',
'Kazakhstan': 'Kazachstan', 'Kenya': 'Kenia', 'Kuwait': 'Kuwejt', 'Kyrgyzstan': 'Kirgistan',
'Laos': 'Laos', 'Latvia': 'Lotwa', 'Lebanon': 'Liban', 'Liberia': 'Liberia', 'Libya': 'Libia', 'Liechtenstein': 'Liechtenstein', 'Lithuania': 'Litwa', 'Luxembourg': 'Luksemburg', 
'MS%20Zaandam': 'MS Zaandam', 'Macao': 'Makao', 'Madagascar': 'Madagaskar', 'Malawi': 'Malawi', 'Malaysia': 'Malezja', 'Maldives': 'Malediwy', 'Mali': 'Mali', 'Malta': 'Malta', 'Martinique': 'Martynika', 'Mauritania': 'Mauretania', 'Mauritius': 'Mauritius', 'Mayotte': 'Majotta', 'Mexico': 'Meksyk', 'Moldova': 'Moldawia', 'Monaco': 'Monako', 'Mongolia': 'Mongolia', 'Montenegro': 'Czarnogora', 'Montserrat': 'Montserrat', 'Morocco': 'Maroko', 'Mozambique': 'Mozambik', 'Myanmar': 'Myanmar', 
'Namibia': 'Namibia', 'Nepal': 'Nepal', 'Netherlands': 'Holandia', 'New%20Caledonia': 'Nowa Kaledonia', 'New%20Zealand': 'Nowa Zelandia', 'Nicaragua': 'Nikaragua', 'Niger': 'Niger', 'Nigeria': 'Nigeria', 'North%20America': 'Ameryka polnocna', 'North%20Macedonia': 'Macedonia Polnocna', 'Norway': 'Norwegia',
'Oceania': 'Oceania', 'Oman': 'Oman', 
'Pakistan': 'Pakistan', 'Palestine': 'Palestyna', 'Panama': 'Panama', 'Papua%20New%20Guinea': 'Papua Nowa Gwinea', 'Paraguay': 'Paragwaj', 'Peru': 'Peru', 'Philippines': 'Filipiny', 'Poland': 'Polska', 'Portugal': 'Portugalia', 'Qatar': 'Katar', 
'Romania': 'Rumunia', 'Russia': 'Rosja', 'Rwanda': 'Rwanda', 
'S.%20Korea': 'Poludniowa Korea', 'Saint%20Kitts%20and%20Nevis': 'Saint Kitts i Nevis', 'Saint%20Lucia': 'Swieta Lucia', 'Saint%20Martin': 'Swiety Marcin', 'Saint%20Pierre%20Miquelon': 'Saint Pierre Miquelon', 'San%20Marino': 'San Marino', 'Saudi%20Arabia': 'Arabia Saudyjska', 'Senegal': 'Senegal', 'Serbia': 'Serbia', 'Seychelles': 'Seszele', 'Sierra%20Leone': 'Sierra Leone', 'Singapore': 'Singapur', 'Sint%20Maarten': 'Sint Maarten', 'Slovakia': 'Slowacja', 'Slovenia': 'Slowenia', 'Somalia': 'Somali', 'South%20Africa': 'Afryka Poludniowa', 'South%20America': 'Ameryka Poludniowa', 'South%20Sudan': 'Poludniowy Sudan', 'Spain': 'Hiszpania', 'Sri%20Lanka': 'Sri Lanka', 'St.%20Barth': 'St. Barth', 'Sudan': 'Sudan', 'Suriname': 'Surinam', 'Sweden': 'Szwecja', 'Switzerland': 'Szwajcaria', 'Syria': 'Syria', 
'Taiwan': 'Tajwan', 'Tanzania': 'Tanzania', 'Thailand': 'Tajlandia', 'Timor-Leste': 'Timor Wschodni', 'Togo': 'Togo', 'Trinidad%20and%20Tobago': 'Trynidad i Tobago', 'Tunisia': 'Tunezja', 'Turkey': 'Turcja',
'UK': 'UK', 'USA': 'USA', 'Uganda': 'Uganda', 'Ukraine': 'Ukraina', 'Uruguay': 'Urugwaj', 'Uzbekistan': 'Uzbekistan', 
'Vatican%20City': 'Watykan', 'Venezuela': 'Wenezuela', 'Vietnam': 'Wietnam', 
'Western%20Sahara': 'Sahara Zachodnia', 'World': 'Swiat', 
'Yemen': 'Jemen', 'Zambia': 'Zambia', 'Zimbabwe': 'Zimbabwe'}

#Inne slowa do tlumaczenia
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


LINK='https://coronavirus-19-api.herokuapp.com/countries/'
BLEDY_POLACZENIA={"[Errno 11001] getaddrinfo failed":"Nie moge wczytaj strony"}
BLEDY_JSON={"Country not found":"Nie ma takiego kraju:"}
WSZYSTKIE_KRAJE_PARAM=["kraje"]
WSZYSTKIE_KRAJE=["Sprobuj: CheckCoronaStat"]



def sprawdz_wersje_pythona():
    if sys.version_info<(3,6,0):
        print ("Niestety wymagana wersja pythona to 3.6 albo wyzsza")
        print ("Jednak jezeli chcesz, zeby program dzialal to pozamieniaj f-stringi")
    



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
        #PARAMETRY[counter]=i.capitalize()
        PARAMETRY[counter]=i[0].upper()+i[1:]
        #PARAMETRY[counter]=i    
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

def policz_wypisz_procenty(co,z_ilu):
    odstep2=14
    wynik=str(co)+f" ({(co/z_ilu)*100:.1f}%)"                    
    return f"{wynik:<{odstep2}}"



def wypisz_kraje(kraje):    
    for i in AngielskieSlowa.values():
        odstep1=25
        odstep2=14
        print (f"{i:{odstep1}} ",end='')
        for j in kraje:
            k=j.replace("%20"," ")
            if kraje[j][i]==k:            
                print (f"{PL_EN[j]:<{odstep2}}",end='')
            else:                                      
                if  i==AngielskieSlowa["deaths"]:
                    print(policz_wypisz_procenty(kraje[j][i],kraje[j][AngielskieSlowa["cases"]]),end='')
                elif i==AngielskieSlowa["critical"]:
                    print(policz_wypisz_procenty(kraje[j][i],kraje[j][AngielskieSlowa["cases"]]),end='')
                elif i==AngielskieSlowa["todayCases"]:
                    print(policz_wypisz_procenty(kraje[j][i],kraje[j][AngielskieSlowa["cases"]]),end='')
                elif i==AngielskieSlowa["recovered"]:
                    print(policz_wypisz_procenty(kraje[j][i],kraje[j][AngielskieSlowa["cases"]]),end='')
                else:
                    print (f"{kraje[j][i]:<{odstep2}}",end='')
        print ("")

def wypisz_date ():
    czas=datetime.now()    
    print (f"{'Stan na:':<25} {czas}")







sprawdz_wersje_pythona()
WYBRANE_KRAJE=sprawdz_ilosc_parametrow()
kraje=dodaj_kraje_do_tablicy(WYBRANE_KRAJE)
wypisz_kraje(kraje)
wypisz_date()




    
    


"""
#Niestety, Google blokuje jak się czesto slownik odpytuje
#Zostawilem jednak kod
def PRZETLUMACZ_EN2PL (WYBRANE_KRAJE_):
    moj_url='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=pl&dt=t&q=$'
    for question in WYBRANE_KRAJE_:        
        przetlumaczone=urlopen(moj_url+question)
        HTML_BODY=przetlumaczone.read()
        #print (HTML_BODY)
        wynik=re.search(' [a-zA-Z ]*',str(HTML_BODY))
        wynik=wynik[0].strip()
        PL_EN[question.capitalize()]=wynik.capitalize()
        
"""        
