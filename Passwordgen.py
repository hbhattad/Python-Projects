import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    if length < 6:
        print("Password length should be at least 6 characters for strong security")
        return None
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
if password:
    print("Generated password: ", password)