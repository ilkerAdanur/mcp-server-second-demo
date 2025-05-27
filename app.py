import requests

def convertCurrency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }

    response = requests.get(url, params=params)
    try:
        data = response.json()
    except Exception:
        return {"error": "Invalid JSON response from API", "status_code": response.status_code}

    if response.status_code == 200 and data.get("success", True):
        if "result" in data and data["result"] is not None:
            return {"converted_amount": data["result"]}
        else:
            return {"error": "Conversion result not found", "api_response": data}
    else:
        return {"error": "API request failed", "status_code": response.status_code, "api_response": data}
