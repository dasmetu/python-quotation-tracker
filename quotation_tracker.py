import json

with open("/content/drive/MyDrive/Quotation Tracker/quotations.json","r") as quotation_file:
  quotation_tracker = json.load(quotation_file)

# =========================
# Input Validation
# =========================
def check_for_integer(prompt):
  while True:
    try:
      check_number = int(input(prompt))
      break
    except ValueError:
      print("Please enter a valid number")
  return check_number

def check_for_range(prompt, low, high):
  while True:
    check_number = check_for_integer(prompt)

    if check_number in range(low, high + 1):
      return check_number

    print(f"Please enter a valid number between {low} and {high}")

def check_for_valid_string(prompt,choices):
  while True:
    user_input = input(prompt).upper()
    if user_input in choices:
      return user_input
    print("Please enter a valid choice")


# =========================
# Repeat Check
# =========================

def repeat_check(prompt):
  while True:
    user_input = check_for_valid_string(prompt,["Y","N","YES","NO"])
    if user_input == "Y" or user_input == "YES":
      return True
    else:
      print("Goodbye")
      return False

# =========================
# Quotation Management
# =========================
def add_quotation():
  customer_name = input("Please enter the customer name: ")
  quotation_number = input("Please enter the quotation number: ")
  quotation_price = check_for_integer("Please enter the quotation price: ")
  quotation_description = input("Please describe the quoation: ")
  quotation = {
      "customer":customer_name,
      "quotation-number": quotation_number,
      "price":quotation_price,
      "description":quotation_description
      }
  return quotation

def display_quotations(quotations):
  if not quotations:
    print("No quotations found")
  else:
    for quotation in quotations:
      print(f"Customer: {quotation['customer']}")
      print(f"Quotation Number: {quotation['quotation-number']}")
      print(f"Price: {quotation['price']}")
      print(f"Description: {quotation['description']}")

def search_quotations(quotations):
  found = False
  quotation_number = input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      display_quotations([quote])
      found = True
  if found == False:
    print("Quotation not found")

def quote_deletion(quotations):
  found = False
  quotation_number = input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      display_quotations([quote])
      user_input = check_for_valid_string(
          "Do you really want to delete this quote: ",
          ["Y","N","YES","NO"]
      )
      if user_input == "YES" or user_input == "Y":
        quotations.remove(quote)
        print("Quotation deleted")
      else:
        print("Deletion cancelled")
      found = True
  if found == False:
    print("Quotation not found")

def quote_update(quotations):
  found = False
  quotation_number = input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      print("What do you want to update?")
      print("1 - Customer Name")
      print("2 - Quotation Number")
      print("3 - Quotation Price")
      print("4 - Quotation Description")
      print("5 - Cancel")
      found = True

      choice = check_for_range("Please choose an action: ",1,5)

      if choice == 1:
        customer_name = input("Please enter the new customer name: ")
        quote['customer'] = customer_name

      elif choice == 2:
        quotation_number = input("Please enter the new quotation number: ")
        quote['quotation-number'] = quotation_number

      elif choice == 3:
        price = check_for_integer("Please enter the new quotation price: ")
        quote['price'] = price

      elif choice == 4:
        description = input("Please enter the new quotation description: ")
        quote['description'] = description

      elif choice == 5:
        print('Action Cancelled')

  if found == False:
    print("Quotation not found")

def save_quotations(quotations):
  with open("/content/drive/MyDrive/Quotation Tracker/quotations.json", "w") as quotation_file:
    json.dump(quotations, quotation_file, indent=4)

# =========================
# Main Function
# =========================

def main(quotations):
  repeat_checker = True

  while repeat_checker == True:
    print("1 - Add Quotation")
    print("2 - Display Quotations")
    print("3 - Search Quotations")
    print("4 - Update Quotation")
    print("5 - Delete Quotation")
    print("6 - Exit Program")

    choice = check_for_range("Please choose an action: ",1,6)

    if choice == 1:
      quotations.append(add_quotation())
      save_quotations(quotations)

    elif choice == 2:
      display_quotations(quotations)

    elif choice == 3:
      search_quotations(quotations)

    elif choice == 4:
      quote_update(quotations)
      save_quotations(quotations)

    elif choice == 5:
      quote_deletion(quotations)
      save_quotations(quotations)

    elif choice == 6:
      print("Goodbye")
      break

    repeat_checker = repeat_check("Do you want to do another operation(Y/N):")

main(quotation_tracker)
