from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    try:
        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_user_input():
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency code (e.g., USD): ").upper()
        to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
        return amount, from_currency, to_currency
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
        return None, None, None

def main():
    user_input = get_user_input()

    if user_input:
        amount, from_currency, to_currency = user_input
        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
