import requests
import urllib3
import json
import conf

urllib3.disable_warnings()
url = "https://192.168.1.215"


r = requests.get(url + "/rest/ip/address/*3", auth=(conf.user, conf.clave), verify=False)
print(json.dumps(r.json(), indent=2))

r2 = requests.get(url + "/rest/interface/ether1", auth=(conf.user, conf.clave), verify=False)
print(json.dumps(r2.json(), indent=2))

print(r2.json()["mac-address"]) #filtar por mac
if r2.json()["mac-address"] == "80:8C:29:FC:5C:85": #si cambiamos la MAC por "80:8C:29:FC:5C:86": no funcionara
    print("El equipo no fue cambiado")
else:
    print("Alguien cambio el equipo!!!")

#METODO PATCH
r3 = requests.get(url + "/rest/ip/address?address=192.168.1.215/24", auth=(conf.user, conf.clave), verify=False)
print(json.dumps(r3.json(), indent=2))

cabecera = {"content-type": "application/json"}
body = {"comment": "USACH2022"}

r4 = requests.patch(url + "/rest/ip/address/*3", auth=(conf.user, conf.clave),headers=cabecera, json=body, verify=False)
print(json.dumps(r4.json(), indent=2))


