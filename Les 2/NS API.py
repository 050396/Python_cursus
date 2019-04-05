import requests
import xmltodict

auth_details = ('ashni.khoenkhoen@student.hu.nl', 'Eko3RV9R72w5Fadr1tpJn7jG3lrnhkv9rpk8810El_esd1MM61x6fg')
api_url = 'https://webservices.ns.nl/ns-api-avt?station=Kampen'
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36

    print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)