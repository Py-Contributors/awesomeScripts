import numpy as np


def convertToNumbers(string):
    string = string.strip().replace(" ", "")
    if len(string) % 2:
        string = string + 'z'
    result = [ord(i) - 97 for i in string]
    return np.reshape(result, (len(result) // 2, 2))


def getmodularInverse(d):
    for i in range(26):
        if (i * d) % 26 == 1:
            break
    return i


def getInverseMatrix(key):
    return [[key[1][1], (-key[0][1]) % 26], [(-key[1][0]) % 26, key[0][0]]]


def getInverseKey(key):
    determinant = int(np.linalg.det(key)) % 26
    inverseDeterminant = getmodularInverse(determinant)
    inverse = getInverseMatrix(key)

    def scalarMulti(x):
        return (inverseDeterminant * x) % 26
    scalarMultiVect = np.vectorize(scalarMulti)
    return scalarMultiVect(np.array(inverse))


def encryptDecrypt(text, key, op):

    keyMatrix = convertToNumbers(key)
    textMatrix = convertToNumbers(text)
    if op == 'd':
        keyMatrix = getInverseKey(keyMatrix)
    resultString = ""
    for col in textMatrix:
        col = np.matmul(keyMatrix, col)
        col = [chr(i % 26 + 97) for i in col]
        resultString = resultString + col[0] + col[1]
    return resultString


if __name__ == "__main__":
    print("==================== 2x2 Hill Cipher =================\n")
    print("Do you want to Encrypt or Decrypt (e/d)? :", end=" ")
    op = input()
    if op not in ['e', 'd']:
        print("Invalid Option")
    else:
        print("Enter the text: ", end=" ")
        text = input()
        print("Enter key (Press enter to use default): ", end=" ")
        key = input()

        if len(key) != 4:
            key = 'hill'
            print("\nUsing default key 'hill'")

        print("\nThe {}crypted text is {}".format(
              'en' if op == 'e' else 'de',
              encryptDecrypt(text, key, op)))
