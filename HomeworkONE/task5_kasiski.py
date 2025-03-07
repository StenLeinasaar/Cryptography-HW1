from collections import defaultdict


def find_repeated_sequences(ciphertext, min_L=3, max_L=6):
    """
    Find all repeated sequences in the ciphertext and calculate distances between consecutive occurrences.

    Args:
        ciphertext (str): The input ciphertext
        min_L (int): Minimum length of sequences to consider
        max_L (int): Maximum length of sequences to consider

    Returns:
        list: List of distances between consecutive occurrences of repeated sequences
    """
    # Dictionary to store positions of each sequence
    pos_dict = defaultdict(list)

    # Check sequences of lengths min_L to max_L
    for L in range(min_L, max_L + 1):
        for i in range(len(ciphertext) - L + 1):
            s = ciphertext[i : i + L]
            pos_dict[s].append(i)

    # Calculate distances between consecutive occurrences
    distances = []
    for s, positions in pos_dict.items():
        if len(positions) > 1:  # Only consider sequences that repeat
            for j in range(1, len(positions)):
                dist = positions[j] - positions[j - 1]
                distances.append(dist)

    return distances


def count_divisible_distances(distances, max_k=20):
    """
    Count how many distances are divisible by each possible key length k.

    Args:
        distances (list): List of distances between repeated sequences
        max_k (int): Maximum key length to consider

    Returns:
        list: Counts of distances divisible by each k from 0 to max_k
    """
    counts = [0] * (max_k + 1)
    for d in distances:
        for k in range(2, max_k + 1):
            if d % k == 0:  # use mod to find exact divisons without remainder
                counts[k] += 1
    return counts


def kasiski_examination(ciphertext):
    """
    Perform the Kasiski examination to estimate the Vigenère cipher key length.

    Args:
        ciphertext (str): The input ciphertext

    Returns:
        tuple: (likely key length, list of counts for each k)
    """
    # Clean the ciphertext: remove whitespace and convert to uppercase
    ciphertext = "".join(ciphertext.split()).upper()

    # Find distances between repeated sequences
    distances = find_repeated_sequences(ciphertext)
    if not distances:
        print("No repeated sequences found.")
        return None, None

    # Count divisible distances up to max_k
    max_k = 20
    counts = count_divisible_distances(distances, max_k)

    # Find the k with the highest count (excluding k=1)
    likely_k = max(range(2, max_k + 1), key=lambda k: counts[k])

    return likely_k, counts


# Example usage
ciphertext = """
FHKOJASZAFUDTBJQLVMKFHKZKFWGACXWGGUMNGAVKSNWEWWNMPANKWHFHKUIXI
JMFEUJLGZLEBJDOAOJMDUWTKOAEGDEZZAUNMBQAPKVPQAXTATEGLNQSYVKOKCIUM
LCIAEHGXRKTUXQUNZVGIGXGHRITLQDSOVVTEXQITTJQTQCZQQZBABRQEBMUFHKXQX
TKZIQIYBYMSCWTFHZEQXOISGPDUWTEATLCFROKMETGQTOAYMKRYUCOQTNQOIHKVA
AUCMTQLGBGROXKNMSYPGIOATFPRUXYMSZMRMPKZDMSQMVEOTGQGRNMCPPATN
DUMAHDOSCPPEXGQGRLMGFPKTVKOAEKFHHQVEOLKJMLQWTENKIMGPHMJUNJGQGIT
DKEIHTGSRGJAAUXVQEEGVFECXMGOHMWVKOAZEANQ
"""


likely_k, counts = kasiski_examination(ciphertext)
if likely_k is not None:
    print(f"Likely key length: {likely_k}")
    print("Counts of distances divisible by each k:")
    for k in range(2, 21):
        print(f"k={k}: {counts[k]}")
