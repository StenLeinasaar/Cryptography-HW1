import string


def index_of_coincidence(text):
    """
    Computes the Index of Coincidence (IC) of a given text.

    The Index of Coincidence (IC) is a measure of the likelihood that two randomly selected letters from a
    ciphertext or plaintext will be the same. It is often used in cryptography, particularly for analyzing
    the frequency distribution of letters in a text, to detect the use of ciphers like the Caesar cipher.

    Parameters:
    - text (str): The input text for which the Index of Coincidence is to be calculated.

    Returns:
    - float: The Index of Coincidence of the input text, a value between 0 and 1.

    How it works:
    1. The function counts the frequency of each letter in the input text.
    2. The formula for IC is used
    3. The IC is undefined for texts with fewer than two letters.

    Example:
    index_of_coincidence("HELLO")
    Returns: 0.04
    """

    # Convert the text to uppercase to ensure case insensitivity
    text = text.upper()

    # Initialize a dictionary to store the frequency of each letter
    freq = {letter: 0 for letter in string.ascii_uppercase}

    # Count the frequency of each letter in the text
    for char in text:
        if char in freq:
            freq[char] += 1

    # Calculate the length of the text
    N = len(text)

    # Return 0 for texts with fewer than 2 characters as IC is undefined for such texts
    if N < 2:
        return 0

    # Calculate the Index of Coincidence using the formula
    ic = sum(freq[letter] * (freq[letter] - 1) for letter in freq) / (N * (N - 1))

    return ic


def average_ic_for_key_length(ciphertext, k):
    """
    Computes the average Index of Coincidence (IC) for the subsequences of a given ciphertext,
    grouped by key length.

    The purpose of this function is to estimate the average IC for different subsequences created by grouping
    the ciphertext into `k` subsequences. This can be useful in cryptanalysis, particularly for ciphers like
    the Vigenère cipher, where the text is divided into multiple groups based on the key length.

    Parameters:
    - ciphertext (str): The encrypted text (ciphertext) to be analyzed.
    - k (int): The assumed key length. The ciphertext will be split into `k` subsequences based on this key length.

    Returns:
    - float: The average Index of Coincidence for the `k` subsequences of the ciphertext.

    How it works:
    1. The ciphertext is cleaned by removing spaces and newlines and converting all letters to uppercase.
    2. The ciphertext is divided into `k` subsequences. Each subsequence contains characters that correspond
       to a particular position in the key.
    3. The IC is calculated for each subsequence. If a subsequence has fewer than 2 characters, it is ignored.
    4. The function returns the average IC value across all valid subsequences.

    Example:
    average_ic_for_key_length("LXFOPVEFRNHR", 3)
    Returns: Average IC value based on subsequences of length >= 2.
    """

    # Clean the ciphertext by converting to uppercase and removing spaces and newlines
    ciphertext = ciphertext.upper().replace(" ", "").replace("\n", "")

    # Create a list to hold the subsequences (one subsequence for each position in the key)
    subsequences = ["" for _ in range(k)]

    # Divide the ciphertext into subsequences based on the key length (k)
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:
            subsequences[i % k] += char

    # Calculate the Index of Coincidence for each subsequence that has at least 2 characters
    ics = [index_of_coincidence(subseq) for subseq in subsequences if len(subseq) >= 2]

    # Return the average IC if there are valid subsequences; otherwise, return 0
    return sum(ics) / len(ics) if ics else 0


# The full ciphertext
ciphertext = """
FHKOJASZAFUDTBJQLVMKFHKZKFWGACXWGGUMNGAVKSNWEWWNMPANKWHFHKUIXI
JMFEUJLGZLEBJDOAOJMDUWTKOAEGDEZZAUNMBQAPKVPQAXTATEGLNQSYVKOKCIUM
LCIAEHGXRKTUXQUNZVGIGXGHRITLQDSOVVTEXQITTJQTQCZQQZBABRQEBMUFHKXQX
TKZIQIYBYMSCWTFHZEQXOISGPDUWTEATLCFROKMETGQTOAYMKRYUCOQTNQOIHKVA
AUCMTQLGBGROXKNMSYPGIOATFPRUXYMSZMRMPKZDMSQMVEOTGQGRNMCPPATN
DUMAHDOSCPPEXGQGRLMGFPKTVKOAEKFHHQVEOLKJMLQWTENKIMGPHMJUNJGQGIT
DKEIHTGSRGJAAUXVQEEGVFECXMGOHMWVKOAZEANQ
""".replace(
    "\n", ""
).upper()


# Test key lengths from 1 to 15
for k in range(1, 16):
    avg_ic = average_ic_for_key_length(ciphertext, k)
    print(f"Key length {k}: Average IC = {avg_ic:.4f}")
