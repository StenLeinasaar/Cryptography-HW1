# Define the ciphertext as a list of three bytes (converted from binary to decimal)
C = [int("00010010", 2), int("00000111", 2), int("11101010", 2)]  # [18, 7, 234]


# Function to check if a byte is an ASCII letter (A-Z or a-z)
def is_letter(byte):
    return (65 <= byte <= 90) or (97 <= byte <= 122)


# Bruteforce all possible 24-bit keys
for K in range(2**24):
    # Extract three bytes from K (big-endian)
    K_bytes = [(K >> 16) & 0xFF, (K >> 8) & 0xFF, K & 0xFF]
    # Compute P = C XOR K for each byte
    P_bytes = [C[i] ^ K_bytes[i] for i in range(3)]
    # Check if all three bytes are letters
    if all(is_letter(P_bytes[i]) for i in range(3)):
        # Convert bytes to characters and form the string
        P_str = "".join(chr(P_bytes[i]) for i in range(3))
        print(P_str)

# Note: This will print around 140,000 three-letter strings.
# To find the message, look for recognizable English words in the output,
# e.g., "the", "cat", "key".
# For efficiency in practice, you could add a dictionary check, but I was too lazy to add it and it was not needed to prove a point.
