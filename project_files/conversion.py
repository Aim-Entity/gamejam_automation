from currency_converter import CurrencyConverter

c = CurrencyConverter()


def converter(value, fromCurrency, toCurrency):
    try:
        return c.convert(value, fromCurrency.upper(), toCurrency.upper())
    except ValueError:
        return "Currency chosen is not supported"


print(converter(100, "EUR", "OOA"))
