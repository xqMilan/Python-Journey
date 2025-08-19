import currencyapicom
import requests

url = "https://api.currencyapi.com/v3/latest"
headers = {
    'apikey': 'cur_live_ncCmcsPeDDbnFtUtuXkJmUplZNTKPw8SXCqrUaFU'
}
response = requests.get(url, headers=headers)
data = response.json()

startwaehrung = input("Gebe deine start Waehrung ein:")
zielwaehrung = input("Gebe deine ziel Waehrung ein:")
betrag = float(input("Gebe deinen Betrag ein: "))

if startwaehrung in data['data'] and zielwaehrung in data['data']:
    start_rate = data['data'][startwaehrung]['value']
    ziel_rate = data['data'][zielwaehrung]['value']

    betrag_in_usd = betrag / start_rate
    ergebnis = betrag_in_usd * ziel_rate
    
    print(f"{betrag} {startwaehrung} = {ergebnis:.2f} {zielwaehrung}")
else:
    print("Ungültige Währung!")