""" Password Checker Tool
Password Checker tool is a password tool that can generate and check
multiple passwords given by the user
"""

__author__ = "Dorian Cruveiller"
__contact__ = "dcruveiller@myges.fr"
__date__ = "2023/06/13"
__deprecated__ = False
__email__ =  "dcruveiller@myges.fr"
__license__ = "UNLICENSED"
__maintainer__ = "developer"
__version__ = "0.0.1"

import sys
import re
import secrets
import string

# password check constants
CHECK_LENGTH = 10
CHECK_NUMBER = 2
CHECK_SPECIAL_CHAR = 1
CHECK_DUMB_PASSWORD_LIST = [
  "azer", "Azer", "AzEr", "aZeR", "AZER", "qwer", "QWER", "123", "321"
]

# password generation constants
GENERATION_MIN_NUMBER = 1
GENERATION_MAX_NUMBER = 20
GENERATION_MIN_LENGTH = 15
GENERATION_MAX_LENGTH = 20

# trash password constants
SHITTY_PASSWORD_FILENAME = "shitty_passwords.txt"

def display_menu():
  """
  Display a menu showing the user how to use this program with multiple actions

    Return:
      what the user choosen as a string

  """
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
  """
  Counts the number of numbers in a string given as argument

  Args:
    string: the string to be checked

  Return:
    the number of a number appeared in the string
  """
  number_count = 0
  for character in string:
    if character.isdigit():
      number_count += 1

  return number_count

def count_special_char(string):
  """
  Counts the number of special characters in a string given as argument

  Args:
    string: the string to be checked

  Return:
    the number of a special characters appeared in the string
  """
  matches = re.findall(r"\W", string)
  return len(matches)
  
def is_dumb_password(string):
  """
  Check if the given string contains dumb substring in it

  Args:
    string: the string to be checked

  Return:
    boolean value representing if dumb password is contained in the string
  """

  for password in CHECK_DUMB_PASSWORD_LIST:
    if password in string:
      return True
  return False

def does_char_identic(string):
  """
  Check if a given string contain the same character in a row

  Args:
    string: the string to be checked

  Return:
    boolean value representing if string contain the same character in a row
  """
  matches = re.findall(r"(.)\1+", string)
  if len(matches) >= 1:
    return True
  return False

def is_palindrome(string):
  """
  Check if a given string is equal to his reversed version

  Args:
    string: the string to be checked

  Return:
    boolean value representing if string is equal to his reversed version
  """
  reversed_string = string[::-1]
  if reversed_string == string:
    return True
  return False

def write_shitty_password(string):
  """
  Write a file containing the string given as argument, this function is meant to write shitty password into a file

  Args:
    string: the string to be written into the file
  """
  file = open(SHITTY_PASSWORD_FILENAME, 'a')
  file.write(f"{string}\n")
  file.close()

def is_valid_password(password, verbose = False):
  """
  Check if a given password is a valid one

  Args:
    password: the password to be checked

  Return:
    boolean value representing if the password is valid or not
  """

  if len(password) < CHECK_LENGTH:
    if verbose:
      print(f"the length is less than {CHECK_LENGTH}")
  elif count_number(password) < CHECK_NUMBER:
    if verbose:
      print(f"contains less than {CHECK_NUMBER} numbers")
  elif count_special_char(password) < CHECK_SPECIAL_CHAR:
    if verbose:
      print(f"contains less than {CHECK_SPECIAL_CHAR} special charaters")
  elif is_dumb_password(password):
    if verbose:
      print("contains a dumb substring password")
  elif does_char_identic(password):
    if verbose:
      print("contains two or more identical characters in a row")
  elif is_palindrome(password):
    if verbose:
      print("this password is a palindrome")
  else:
    return True
  
  write_shitty_password(password)

  return False

def generate_password(length):
  """
  Generate a password with the specified length specified as agument

  Args:
    length: the password length

  Return:
    string representing the generated password
  """
  alphabet = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(secrets.choice(alphabet) for i in range(length))
  return password


# ================== HANDLER ==================

def handle_password_checking():
  """
  Handle the password check, this function is called from main
  """
  password = input("Enter the password to be checked: ")
  if is_valid_password(password, True):
    print("This password is safe to use")
  else:
    print("This password is shitty")

def handle_password_generation():
  """
  Handle the password generation, this function is called from main
  """
  password_number = -1
  while (password_number == -1):
    choosen_number = input(f"Enter the number of passwords to be generated [{GENERATION_MIN_NUMBER}-{GENERATION_MAX_NUMBER}]: ")
    if choosen_number.isdigit():
      choosen_number = int(choosen_number)
      if choosen_number >= GENERATION_MIN_NUMBER and choosen_number <= GENERATION_MAX_NUMBER:
        password_number = choosen_number

  for i in range(password_number):
    password_size = secrets.choice(range(GENERATION_MIN_LENGTH, GENERATION_MAX_LENGTH + 1))
    password = generate_password(password_size)
    while (is_valid_password(password) == False):
      password = generate_password(password_size)

    print(f"password {i + 1}: {password}")

# main function
def main():
  """
  This function is the main function of this script and is responsible for the all script
  """
  while (True):
    chosen_action = display_menu()
    if chosen_action.isdigit() == True:
      chosen_action = int(chosen_action)

      if chosen_action == 1:
        handle_password_checking()
      elif chosen_action == 2:
        handle_password_generation()
      elif chosen_action == 3:
        print("See you soon :)")
        print(f"Made by {__author__} on {__date__}")
        sys.exit()

# Start script
main()