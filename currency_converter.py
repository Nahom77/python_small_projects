
CURRENCIES = ('USD', 'EUR', 'CAD')

CONVERSION_RATE = {
    'USD': {'EUR': 1.1, 'CAD': 1.2},
    'EUR': {'USD': 0.11, 'CAD': 0.3},
    'CAD': {'EUR': 3, 'USD': 0.12}
}

def get_amount() :
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print('Enter a valid amount')

def get_currency(label) :
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if (currency not in CURRENCIES):
            print('Invalid currency')
        else:
            return currency

def convert_currencies() :
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')

    if(source_currency == target_currency) :
        converted_amount = amount
    else:
        converted_amount = amount * CONVERSION_RATE[source_currency][target_currency]

    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} of {target_currency}')

convert_currencies()