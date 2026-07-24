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
      "quotation-number":"T-"+quotation_number,
      "price":quotation_price,
      "description":quotation_description
      }
  return quotation

def display_quotations(quotations):
  for quotation in quotations:
    print(f"Customer: {quotation['customer']}")
    print(f"Quotation Number: {quotation['quotation-number']}")
    print(f"Price: {quotation['price']}")
    print(f"Description: {quotation['description']}")

def search_quotations(quotations):

  found = False
  quotation_number = "T-" + input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      print(quote)
      found = True
  if found == False:
    print("Quotation not found")
    

# =========================
# Main Function
# =========================

def main():
  quotations = []
  repeat_checker = True
  while repeat_checker == True:
    print("1 - Add Quotation")
    print("2 - Display Quotations")
    print("3 - Search Quotations")
    print("4 - Exit Program")
    choice = check_for_range("Please choose an action: ",1,4)
    if choice == 1:
      quotations.append(add_quotation())
      repeat_checker = repeat_check("Do you want to do another operation(Y/N):")
    elif choice == 2:
      display_quotations(quotations)
      repeat_checker = repeat_check("Do you want to do another operation(Y/N): ")
    elif choice == 3:
      search_quotations(quotations)
      repeat_checker = repeat_check("Do you want to do another operation(Y/N):")
    elif choice == 4:
      print("Goodbye")
      break
