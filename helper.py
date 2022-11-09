#!/usr/bin/env python3
"""MDalavai | helper functions for Currency Converter"""

import json
import pprint
import requests

#function to list all currencies 
def list_currencies():
   
    """List of Currencies"""
    
    url = "https://api.fastforex.io/currencies?api_key=67f42a4e33-1fcc5e9d1e-rj7nis"
    
    data = requests.get(url)
    result = data.json()
    for i in result["currencies"]:
        print(i, end="-------")
        pprint.pprint(result["currencies"][i])
    print("---------------------------------------------------------")    
    print(f"Total Number of Currencies : {len(result['currencies'])}")
    print("---------------------------------------------------------")

#function exchange rates
def exchange_rate(currency1, currency2):
    
    """Exchange rates"""
    url = "https://currency-converter-pro1.p.rapidapi.com/latest-rates"
    
    currency1 = "USD"
    
    

    querystring = { "base" : currency1, "currencies" : currency2 }
    headers = {
    	"X-RapidAPI-Key": "f28ba617dcmshd66f7ecf9ae61c6p17dd07jsne9a5c2bce5ed",
    	"X-RapidAPI-Host": "currency-converter-pro1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    if len(data) == 0:
        print('Invalid currencies.')
        return
    rate = data.get("result").get(currency2)
    print(f"{currency1} -> {currency2} = {rate}")
