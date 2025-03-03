import matplotlib.pyplot as plt
import collections
import string
import random


# Function to read plaintext from a file
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


# Function to compute letter frequencies
def letter_frequency(text):
    text = text.lower()
    freq = collections.Counter(c for c in text if c in string.ascii_lowercase)
    return freq


# Function to plot and save frequency diagram
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
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return "".join(result)


# Permutation Cipher Encryption (Monoalphabetic substitution)
def permutation_cipher(text):
    shuffled = list(string.ascii_lowercase)
    random.shuffle(shuffled)
    mapping = str.maketrans(string.ascii_lowercase, "".join(shuffled))
    return text.lower().translate(mapping)


# Vigenère Cipher Encryption
def vigenere_cipher(text, key="KEY"):
    result = []
    key = key.lower()
    key_length = len(key)
    for i, char in enumerate(text.lower()):
        if char in string.ascii_lowercase:
            shift = ord(key[i % key_length]) - ord("a")
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(char)
    return "".join(result)


# Read plaintext from file
plaintext = read_plaintext("./HomeworkONE/plaintext_task2.txt")
if plaintext:
    # Encrypting plaintext
    shift_encrypted = shift_cipher(plaintext)
    perm_encrypted = permutation_cipher(plaintext)
    vigenere_encrypted = vigenere_cipher(plaintext)

    # Compute frequencies
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
