def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord("A")  # shifting
            encrypted_char = chr(
                ((ord(char) - ord("A") + shift) % 26) + ord("A")
            )  # Modulos calculation
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


# Given message and key
message = "THEWANDCHOOSESTHEWIZARD"
message2 = "THELANDCHOOSESTHELIZARD"
key = "MAGIC"
key2 = "MANIC"

# Encrypt the message
encrypted_message1 = vigenere_encrypt(message, key)
encrypted_message2 = vigenere_encrypt(message2, key)
print("Encrypted Message:", encrypted_message1)
print("Encrypted Message:", encrypted_message2)

encrypted_message1 = vigenere_encrypt(message, key2)
encrypted_message2 = vigenere_encrypt(message2, key2)
print("Encrypted with new key Message:", encrypted_message1)
print("Encrypted with new key Message:", encrypted_message2)
