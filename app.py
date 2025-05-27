import requests

def convertCurrency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return {"converted_amount": data["result"]}
        else:
            return {"error": "Conversion result not found"}
    else:
        return {"error": "API request failed"}
