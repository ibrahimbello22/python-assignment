# Caesar Cipher Program

def encrypt(message, shift):
    encrypted = ""

    for char in message:
        if char.isalpha():
            # Check if uppercase or lowercase
            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Keep spaces and symbols unchanged
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted += char

    return decrypted


# User input
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Encrypt message
encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

# Decrypt message
decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)