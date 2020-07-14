import random
import array

# Max length of the password
MAX_LENGTH = 12

# Declare arrays of charaters needed to create password.
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<&# 039;']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# Randomly select atleast one character from each set above
random_digit = random.choice(DIGITS);
random_lower = random.choice(LOCASE_CHARACTERS)
random_upper = random.choice(UPCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)

temp_pass = random_digit + random_lower + random_upper + random_symbol
for x in range(MAX_LENGTH-4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    # convert temporary password  into array and shuffle to prevent it from having a consistent pattern
    temp_pass_list = array.array("u", temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x;

print(password)

