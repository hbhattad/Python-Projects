from cryptography.fernet import Fernet

# Get input from user
message = input("Enter Message: ")

# Generate a key for encryption and decryption
key = Fernet.generate_key()

# Instance the Fernet class with the key
fernet = Fernet(key)

# Encode the input message to bytes before encryption
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# Decrypt the encrypted string with the Fernet instance of the key,
# that was used for encrypting the string.
# Encoded byte string is returned by decrypt method, so decode it to string.
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
