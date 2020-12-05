from currency_converter import CurrencyConverter

c = CurrencyConverter()  # Python API (Only europe conversion)


def converter(value, fromCurrency, toCurrency):
    try:
        return c.convert(value, fromCurrency.upper(), toCurrency.upper())
    except ValueError:
        return "Currency chosen is not supported"
