import numpy as np

# Key matrix
keyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Following function generates the key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Encryption function
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipherEncrypt(message, key):
    # Get key matrix from the key string
    getKeyMatrix(key)

    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Generate the encrypted vector
    encrypt(messageVector)

    # Generate the encrypted text
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    # Join the ciphertext into a string
    cipher_str = "".join(CipherText)

    # Return the ciphertext string
    return cipher_str

# Function to compute modular inverse of a number modulo m
def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Find the cofactor matrix
def getCofactorMatrix(mat):
    cofactor = np.zeros((3, 3))
    cofactor[0][0] = mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]
    cofactor[0][1] = -(mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
    cofactor[0][2] = mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]
    cofactor[1][0] = -(mat[0][1] * mat[2][2] - mat[0][2] * mat[2][1])
    cofactor[1][1] = mat[0][0] * mat[2][2] - mat[0][2] * mat[2][0]
    cofactor[1][2] = -(mat[0][0] * mat[2][1] - mat[0][1] * mat[2][0])
    cofactor[2][0] = mat[0][1] * mat[1][2] - mat[0][2] * mat[1][1]
    cofactor[2][1] = -(mat[0][0] * mat[1][2] - mat[0][2] * mat[1][0])
    cofactor[2][2] = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    return cofactor

# Inverse of the key matrix modulo 26
def getInverseKeyMatrix(keyMatrix):
    det = int(np.round(np.linalg.det(keyMatrix))) % 26
    invDet = modInverse(det, 26)

    if invDet == -1:
        print("Inverse doesn't exist for the given key matrix!")
        return None

    cofactorMatrix = getCofactorMatrix(keyMatrix)
    adjointMatrix = cofactorMatrix.T
    inverseMatrix = (invDet * adjointMatrix) % 26

    return inverseMatrix.astype(int)

# Decryption function
def decrypt(cipherMatrix, keyMatrix):
    inverse_keyMatrix = getInverseKeyMatrix(keyMatrix)

    if inverse_keyMatrix is None:
        return None

    decryptedMatrix = np.dot(inverse_keyMatrix, cipherMatrix) % 26

    # Generate the decrypted text
    decryptedText = []
    for i in range(3):
        decryptedText.append(chr(int(decryptedMatrix[i][0]) + 65))

    return "".join(decryptedText)

# Function to implement Hill cipher decryption
def HillCipherDecrypt(cipherText, key):
    # Get key matrix from the key string
    getKeyMatrix(key)

    # Generate vector for the cipher text
    for i in range(3):
        cipherMatrix[i][0] = ord(cipherText[i]) % 65

    # Decrypt the cipher text
    decryptedText = decrypt(cipherMatrix, keyMatrix)

    if decryptedText:
        print("Decrypted Text: ", decryptedText)

# Driver code
def main():
    # Encryption
    message = "ACT"
    key = "GYBNQKURP"
    ciphertext = HillCipherEncrypt(message, key)
    print("Ciphertext: ", ciphertext)

    # Decryption
    cipherText = ciphertext  # Use the ciphertext from the encryption
    HillCipherDecrypt(cipherText, key)

if __name__ == "__main__":
    main()
