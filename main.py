FILEPATH = "quotations.json"

from validation import *
from quotation_manager import *
from storage import *


def main(quotations):
  repeat_checker = True

  while repeat_checker:
    print("1 - Add Quotation")
    print("2 - Display Quotations")
    print("3 - Search Quotation")
    print("4 - Update Quotation")
    print("5 - Delete Quotation")
    print("6 - Exit Program")

    choice = check_for_range("Please choose an action: ",1,6)

    if choice == 1:
      quotations.append(add_quotation(quotations))
      save_quotations(quotations)

    elif choice == 2:
      display_quotations(quotations)

    elif choice == 3:
      search_quotation(quotations)

    elif choice == 4:
      update_quotation(quotations)
      save_quotations(quotations)

    elif choice == 5:
      delete_quotation(quotations)
      save_quotations(quotations)

    elif choice == 6:
      print("Goodbye")
      break

    repeat_checker = repeat_check("Do you want to do another operation(Y/N):")

quotations = load_quotations()
main(quotations)
