def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another using exchangerate.host API.
    """
    import requests

    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        result = data.get("result")
        return {"converted_amount": result}
    else:
        return {"error": "Failed to retrieve data from currency API"}
