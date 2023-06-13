import sys
import re
import secrets
import string

def display_menu():

  print("#############################################################################")
  print("########                                                             ########")
  print("########                   Password Checker Tool'                    ########")
  print("######## ----------------------------------------------------------- ########")
  print("########                This tool give you the ability               ########")
  print("########                to check and generate password               ########")
  print("######## ----------------------------------------------------------- ########")
  print("########                                                             ########")
  print("########                      Choose an action:                      ########")
  print("########                                                             ########")
  print("########        1) Check a password  |  2) Generate passwords        ########")
  print("########                           3) Exit                           ########")
  print("########                                                             ########")
  print("#############################################################################")

  return input("Choose an action: ")

def count_number(string):
  number_count = 0
  for character in string:
    if character.isdigit():
      number_count += 1

  return number_count

def count_special_char(string):
  matches = re.findall(r"\W", string)
  return len(matches)
  
def is_dumb_password(string):
  dumb_passwords = [
    "azer", "Azer", "AzEr", "aZeR", "AZER", "qwer", "QWER", "123", "321"
  ]

  for password in dumb_passwords:
    if password in string:
      return True
  return False

def does_char_identic(string):
  matches = re.findall(r"(.)\1+", string)
  if len(matches) >= 1:
    return True
  return False

def is_palindrome(string):
  reversed_string = string[::-1]
  if reversed_string == string:
    return True
  return False

def handle_password_generation():

  password_number = -1

  while (password_number == -1):
    choosen_number = input("Enter the number of passwords to be generated [1-20]: ")
    if choosen_number.isdigit():
      choosen_number = int(choosen_number)
      if choosen_number >= 1 and choosen_number <= 20:
        password_number = choosen_number

  alphabet = string.ascii_letters + string.digits + string.punctuation

  for i in range(password_number):

    password_size = secrets.choice(range(10, 20 + 1))

    password = ''

    while (check_password(password) == False):
      password = ''.join(secrets.choice(alphabet) for i in range(password_size))

    print(f"password {i + 1}: {password}")

def check_password(password):
  if len(password) >= 10 and count_number(password) >= 2 and count_special_char(password) >= 1 and is_dumb_password(password) == False and does_char_identic(password) == False and is_palindrome(password) == False:
    return True
  return False

while (True):
  chosen_action = display_menu()
  if chosen_action.isdigit() == True:
    chosen_action = int(chosen_action)

    if chosen_action == 1:
      password = input("Enter the password to be checked: ")
      if check_password(password):
        print("This password is safe to use")
      else:
        print("This password is trash")
    elif chosen_action == 2:
      handle_password_generation()
    elif chosen_action == 3:
      print("See you soon :)")
      sys.exit()
