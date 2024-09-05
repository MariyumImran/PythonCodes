import random
import string

password_length = int(input("How long do you want the password to be?   "))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

all_characters = lowercase + uppercase + digits + special_characters

password = ''.join(random.choice(all_characters) for _ in range(password_length))

print("Generated Password:", password)