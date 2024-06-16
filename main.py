import requests
import json

url = "https://api.pokemontcg.io/v2/cards?q="
sID = input("Please enter the Set ID [EX: twm]:")
cID = input("Please enter the card number:")
newurl = url+"set.ptcgoCode:"+sID+" AND number:"+cID

r = requests.get(newurl)

if r.status_code == 200:
    data = r.json()
    card_info = data['data'][0]
    prices = card_info['cardmarket']['prices']
    setinfo = card_info['set']
    avgsell = prices['averageSellPrice']
    print("Card ID:", card_info['id'])
    print("Card Name:",card_info['name'])
    print("Card Rarity:",card_info['rarity'])
    print("Card Set:",setinfo['name'])
    print(f"AVG Sell Price: ${avgsell}")

else:
    print(f"Failed to retrieve data. HTTP ERROR CODE: {r.status_code}")