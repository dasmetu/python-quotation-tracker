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

def check_for_non_blank(prompt):
  while True:
    check_string = input(f"Please enter a {prompt}: " )
    check_string = check_string.strip()
    if check_string != "":
      return check_string
    print(f"This is not a valid {prompt}.")

def check_for_negative(prompt):
  while True:
      check_number = check_for_integer(prompt)
      if check_number < 0:
        print("The input number can not be negative")
      else:
        return check_number

def check_for_duplicate(items,prompt,key,current_item = 0):
  while True:
    duplicate = False
    check_variable = input(prompt)
    for i in items:
      if check_variable == i[key] and current_item != i:
        duplicate = True
    if duplicate:
      print("Duplicate Found")
    else:
      return check_variable

# =========================
# Repeat Check
# =========================

def repeat_check(prompt):

  user_input = check_for_valid_string(prompt,["Y","N","YES","NO"])
  if user_input in ["Y","YES"]:
    return True
  
  print("Goodbye")
  return False

