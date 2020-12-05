from project_files.conversion import converter
from project_files.email_sender import email
from project_files.retirement import retire

command = ""
print(">>> Help (for more info)")
print("")

while command != "Quit":
  command = input(">>> ").title()
  print("")

  if command == "Help":
    print("Command List:\n\t- Convert\n\t- Email\n\t- Retirement Calculator")

  if command == "Convert":
    print("Disclaimer: This converter only converts currency across Europe and a handful of other countries. If you want the list of country codes go to:\nhttps://www.iban.com/currency-codes\n")

    value = int(input("Enter Value To Convert: "))
    fromCurrency = input("Enter Country Code To Convert From: ").upper()
    toCurrency = input("Enter Country Code To Convert To: ").upper()

    print(f"{round(converter(value, fromCurrency, toCurrency), 2)} {toCurrency}")
  
  if command == "Email":
    email()
