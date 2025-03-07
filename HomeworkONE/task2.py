import matplotlib.pyplot as plt
import collections
import string
import random


# Function to read plaintext from a file. Error handling included.
def read_plaintext(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""


# Function to compute letter frequencies. Uses counter and puts all text to lowercase for easy counting.
def letter_frequency(text):
    text = text.lower()
    freq = collections.Counter(c for c in text if c in string.ascii_lowercase)
    return freq


# Function to plot and save frequency diagram.
# Simple basics of matplot. Adding title, bar , lables, grid.
def plot_frequency(freq_dict, title, filename):
    letters, counts = zip(*sorted(freq_dict.items()))
    plt.figure(figsize=(10, 5))
    plt.bar(letters, counts, color="#D8BFD8")  # Light purple color
    plt.title(title, fontsize=14, color="purple")
    plt.xlabel("Letters", fontsize=12, color="purple")
    plt.ylabel("Frequency", fontsize=12, color="purple")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(filename, bbox_inches="tight", facecolor="white")
    plt.close()


# Shift Cipher Encryption (Caesar cipher with shift=3)
def shift_cipher(text, shift=3):
    """
    Encrypts or decrypts a given text using a shift cipher (Caesar cipher).

    The shift cipher, also known as the Caesar cipher, is a type of substitution cipher where each letter in the
    text is shifted by a certain number of positions in the alphabet. The same shift is applied for both encryption
    and decryption, making the process reversible.

    Parameters:
    - text (str): The text to be encrypted or decrypted.
    - shift (int): The number of positions to shift each letter. By default, the shift is 3.

    Returns:
    - str: The encrypted or decrypted version of the input text.

    How it works:
    1. Each letter of the text is shifted by the specified number (shift value) in the alphabet.
    2. Uppercase and lowercase letters are treated separately, so case is preserved.
    3. Non-alphabetic characters (such as spaces, punctuation, etc.) remain unchanged.

    Example:
    shift_cipher("Hello World", 3)
    Returns: "Khoor Zruog"
    """

    result = []  # List to store the result of encryption/decryption

    # Iterate through each character in the input text
    for char in text:
        if char.isalpha():  # Check if the character is an alphabetic letter
            # Determine the ASCII value of the base character ('A' for uppercase or 'a' for lowercase)
            shift_base = ord("A") if char.isupper() else ord("a")

            # Shift the character and ensure it wraps around the alphabet using modulo 26
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            # If it's not a letter, just append it unchanged (e.g., spaces, punctuation)
            result.append(char)

    # Join the list of characters into a final string and return the result
    return "".join(result)


# Permutation Cipher Encryption (Monoalphabetic substitution)
def permutation_cipher(text):
    """
    Encrypts or decrypts a given text using a permutation cipher.

    The permutation cipher is a form of substitution cipher where each letter of the alphabet is substituted with another letter,
    based on a random shuffled order of the alphabet. The same shuffled alphabet is used for both encryption and decryption.

    Parameters:
    - text (str): The text to be encrypted or decrypted. The text is converted to lowercase before processing.

    Returns:
    - str: The encrypted or decrypted version of the input text, depending on whether it is the original message or already encrypted.

    How it works:
    1. The alphabet (a-z) is shuffled randomly.
    2. A mapping is created between the original alphabet and the shuffled alphabet.
    3. Each letter in the text is replaced with its corresponding letter from the shuffled alphabet.
    4. Non-alphabetic characters are not altered.

    Example:
    permutation_cipher("Hello World")
    Returns: a randomly shuffled ciphertext
    """

    # Create a list of lowercase letters from a to z
    shuffled = list(string.ascii_lowercase)

    # Shuffle the list of letters randomly
    random.shuffle(shuffled)

    # Create a translation mapping from the original alphabet to the shuffled one
    mapping = str.maketrans(string.ascii_lowercase, "".join(shuffled))

    # Convert the input text to lowercase and apply the translation mapping
    return text.lower().translate(mapping)


# Vigenère Cipher Encryption
def vigenere_cipher(text, key="KEY"):
    """
    Encrypts or decrypts a given text using the Vigenère cipher.

    The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
    A keyword is used to determine the shift of each letter in the plaintext.

    Parameters:
    - text (str): The text to be encrypted or decrypted.
    - key (str): The keyword used for the cipher (default is "KEY"). The key will be repeated as needed to match the length of the text.

    Returns:
    - str: The encrypted or decrypted version of the input text.

    How it works:
    1. The key is repeated as necessary to match the length of the text.
    2. Each character of the text is shifted according to the corresponding character in the key. The shift is based on the position of the character in the alphabet (e.g., 'a' = 0, 'b' = 1, ..., 'z' = 25).
    3. Non-alphabetic characters are not altered.

    Example:
    vigenere_cipher("Hello World", "KEY")
    Returns: ciphertext
    """

    result = []  # List to store the result of encryption/decryption
    key = key.lower()  # Convert the key to lowercase to handle case insensitivity
    key_length = len(key)  # Length of the key

    for i, char in enumerate(text.lower()):
        if char in string.ascii_lowercase:  # Check if the character is a letter
            # Calculate the shift based on the current character of the key
            shift = ord(key[i % key_length]) - ord("a")

            # Apply the Vigenère shift to the current letter
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(
                new_char
            )  # Append the encrypted/decrypted character to the result
        else:
            # If the character is not a letter, just append it as it is (e.g., spaces or punctuation)
            result.append(char)
    # Join the list of characters into a final string and return the result
    return "".join(result)


# Read plaintext from file
plaintext = read_plaintext("./HomeworkONE/plaintext_task2.txt")
if plaintext:
    # Calling encryption functions
    shift_encrypted = shift_cipher(plaintext)
    perm_encrypted = permutation_cipher(plaintext)
    vigenere_encrypted = vigenere_cipher(plaintext)

    # Computing frequencies by calling functions
    plaintext_freq = letter_frequency(plaintext)
    shift_freq = letter_frequency(shift_encrypted)
    perm_freq = letter_frequency(perm_encrypted)
    vigenere_freq = letter_frequency(vigenere_encrypted)

    # Plot and save frequency diagrams
    plot_frequency(plaintext_freq, "Plaintext Letter Frequency", "plaintext_freq.jpg")
    plot_frequency(shift_freq, "Shift Cipher Frequency", "shift_cipher_freq.jpg")
    plot_frequency(
        perm_freq, "Permutation Cipher Frequency", "permutation_cipher_freq.jpg"
    )
    plot_frequency(
        vigenere_freq, "Vigenère Cipher Frequency", "vigenere_cipher_freq.jpg"
    )
