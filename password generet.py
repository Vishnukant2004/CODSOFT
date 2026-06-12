import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
length = int(input("Enter desired password length: "))

# Generate and Display Password
password = generate_password(length)
print("Generated Password:", password)
