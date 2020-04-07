"""
text="poszla szkola do"
lista = list(text.split())
print (lista)
"""
AngielskieSlowa={"testsPerOneMillion":"Testy na milion:",
                 "todayCases":"Dzisiejsze przypadki:",
                 "totalTests":"Ilosc wszystkich testow:",
                 "todayDeaths":"Dzisiejsze zgony:",
                 "deathsPerOneMillion":"Zgony na milion:",
                 "cases":"Wszystkie przypadki:",
                 "active":"Aktywne przypadki:",
                 "deaths":"Zgodny:",
                 "casesPerOneMillion":"Przypadki na milion:",
                 "recovered":"Wyleczeni:",
                 "critical":"W stanie krytycznym:",
                 "country":"Panstwo"}


for i in AngielskieSlowa.keys():
    print (i)
"""
JakiesDane={"testsPerOneMillion":"33"}
JakiesDaneTranslate={}
JakiesDaneTranslate[AngielskieSlowa["testsPerOneMillion"]]=JakiesDane["testsPerOneMillion"]

print (AngielskieSlowa["testsPerOneMillion"])
print (JakiesDane["testsPerOneMillion"])
print (JakiesDaneTranslate)
"""