from validation import *

# =========================
# Quotation Management
# =========================
def add_quotation(quotations):

  quotation = {
      "customer":check_for_non_blank("customer name"),
      "quotation-number": check_for_duplicate(quotations,"Please enter the quotation number: ","quotation-number"),
      "price":check_for_negative("Please enter the quotation price: "),
      "description":input("Please describe the quotation: ")
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

def search_quotation(quotations):

  quotation_number = input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      display_quotations([quote])
      return
  
  print("Quotation not found")

def delete_quotation(quotations):
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
      return
  
  print("Quotation not found")

def update_quotation(quotations):

  quotation_number = input("Please enter the quotation number: ")
  for quote in quotations:
    if quote["quotation-number"] == quotation_number:
      print("What do you want to update?")
      print("1 - Customer Name")
      print("2 - Quotation Number")
      print("3 - Quotation Price")
      print("4 - Quotation Description")
      print("5 - Cancel")
      

      choice = check_for_range("Please choose an action: ",1,5)

      if choice == 1:
        
        quote['customer'] = check_for_non_blank("customer name")

      elif choice == 2:
        
        quote['quotation-number'] = check_for_duplicate(quotations,"Please enter the new quotation number: ","quotation-number",quote)

      elif choice == 3:
        
        quote['price'] = check_for_negative("Please enter the new quotation price: ")

      elif choice == 4:

        quote['description'] = input("Please enter the new quotation description: ")

      elif choice == 5:
        print("Action Cancelled")
    
      return
      
  print("Quotation not found")

