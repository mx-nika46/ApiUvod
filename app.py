# API klici (spletnni klici)

import requests
import pprint #lepše izpiše rezultate

#baseUrl="https://www.google.com/"
#klic = requests.get(baseUrl)

# print(klic) koda odgovor
#print(klic.text) #raw odgovor-t
"""
#api klic z json odgovorom 
baseUrl="https://api.chucknorris.io/jokes/random"
for i in range(10): #dobiš 10 vicov
    klic= requests.get(baseUrl)
    #preverimo .text da je res json
    js=klic.json() #pretvorimo v dict
    #pprint.pprint(js)ž
    print(js.get("value"))
"""




"""
baseUrl="https://api.nationalize.io/?name="
ime="Nika"
klic=requests.get(baseUrl+ime).json()
#print(klic.url)
print(klic)
print(f"{klic.get("count")}")
print(f"{klic.get("name")}")

države=klic.get("country")
for d in države:
    print(d.get("country_id"))
    print(d.get("probability"))
"""

#popravite izpise da bo lepši v %

#cats fact
baseUrl="https://meowfacts.herokuapp.com/"
klic= requests.get(baseUrl).json()
print(klic.get("data"))

