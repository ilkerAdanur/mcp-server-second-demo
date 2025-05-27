import requests

def convertCurrency(amount, from_currency, to_currency):
    """
    Convert currency using exchangerate-api.com free API
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Get exchange rates for the base currency
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        data = response.json()

        # Check if the target currency exists in rates
        if "rates" not in data:
            return {"error": "No exchange rates found in API response"}

        rates = data["rates"]

        if to_currency not in rates:
            return {"error": f"Currency '{to_currency}' not supported"}

        # Calculate conversion
        exchange_rate = rates[to_currency]
        converted_amount = float(amount) * exchange_rate

        return {
            "converted_amount": round(converted_amount, 2),
            "exchange_rate": exchange_rate,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "original_amount": amount
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid amount: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
