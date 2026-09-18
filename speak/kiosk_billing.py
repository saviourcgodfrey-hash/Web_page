def calculate_subtotal(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Inputs cannot be negative!")
    return price * quantity

def apply_discount(total, discount_rate):
    return total * (1.0 - discount_rate)

import requests

def charge_payment_card(card_token, amount_cents):
    """Send a post request to the payment merchant API."""
    payload = {"token": card_token, "amount": amount_cents}
    response = requests.post("https://api.merchant.com/charge", json=payload)
    
    if response.status_code != 200:
        raise ConnectionError("Payment gateway declined transaction!")
    return response.json()