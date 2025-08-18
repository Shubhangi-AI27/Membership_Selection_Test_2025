# Playfair Cipher Decryption (with 'Q' omitted)

def generate_key_square(key):
    key = key.upper().replace(" ", "")   
    key = "".join(dict.fromkeys(key))    

    alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ" 
    key_square = key + "".join([c for c in alphabet if c not in key])

    # Convert to 5x5 matrix
    matrix = [list(key_square[i:i+5]) for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def preprocess_ciphertext(ciphertext):
    ciphertext = ciphertext.upper()
    ciphertext = "".join([c for c in ciphertext if c.isalpha()])
    if len(ciphertext) % 2 != 0:
        ciphertext += "X"  # Padding if needed
    return ciphertext


def decrypt_playfair(ciphertext, key):
    matrix = generate_key_square(key)
    ciphertext = preprocess_ciphertext(ciphertext)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row → move left
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column → move up
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle → swap columns
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


# Main execution block
if __name__ == "__main__":
    # From the problem: Keyword is the subject of the clue "curiosity killed the cat" → CURIOSITY
    key = "CURIOSITY"  
    ciphertext = "KBVE MPBI YXAL SKAY RPMI YSGA TLHE LONP DE"
    
    plaintext = decrypt_playfair(ciphertext, key)
    print("Decrypted message:", plaintext)
