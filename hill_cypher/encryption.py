from hill_cypher.exceptions import SizeMisMatchException


def convert_plain_text_to_cipher(plain_text_matrix, key_matrix, plain_text_size):
    cipher_matrix_iter = 0
    cipher_matrix = [[0] * plain_text_size]
    for i in range(plain_text_size):
        for j in range(plain_text_size):
            cipher_matrix_iter += key_matrix[i][j] * plain_text_matrix[j]
        cipher_matrix[0][i] = cipher_matrix_iter % 26
        cipher_matrix_iter = 0
    return cipher_matrix[0]


def convert_cipher_matrix_to_text(cipher_matrix, plain_text_size):
    cipher_text = ''
    for i in range(plain_text_size):
        cipher_text += chr(cipher_matrix[i] + 65)
    return cipher_text


class HillCypher:

    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = key

    def check_for_matching_key_and_plain_text_size(self, plain_text_size, key_size):
        if key_size % plain_text_size != 0:
            raise SizeMisMatchException()

    def get_n_for_plain_text(self):
        try:
            plain_text_size: int = len(self.plain_text)
            key_size = len(self.key)
            self.check_for_matching_key_and_plain_text_size(plain_text_size, key_size)
            return plain_text_size, key_size
        except SizeMisMatchException:
            print("plain text size is not divisible by key size")

    def encrypt_text(self):
        plain_text_size, key_size = self.get_n_for_plain_text()
        plain_text_matrix = self.change_to_plain_text_matrix(self.plain_text, plain_text_size)
        key_matrix = self.change_to_key_matrix(self.key, key_size, plain_text_size)
        cipher_matrix = convert_plain_text_to_cipher(plain_text_matrix, key_matrix, plain_text_size)
        cipher_text = convert_cipher_matrix_to_text(cipher_matrix, plain_text_size)
        print("cipher_text", cipher_text)

    def change_to_plain_text_matrix(self, plain_text, plain_text_size):
        plain_text_matrix = [[0] * plain_text_size]
        for i in range(plain_text_size):
            plain_text_matrix[0][i] = ord(plain_text[i]) % 65
        return plain_text_matrix[0]

    def change_to_key_matrix(self, key, plain_text_size):
        key_matrix = [[0] * plain_text_size for i in range(plain_text_size)]
        key_iterator: int = 0
        for i in range(plain_text_size):
            for j in range(plain_text_size):
                key_matrix[i][j] = ord(key[key_iterator]) % 65
                key_iterator += 1
        return key_matrix
