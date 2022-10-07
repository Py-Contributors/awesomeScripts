from Crypto.Cipher import AES
from cryptography.fernet import Fernet
import Crypto.Random as Random


class ImageEncryption:
    """
    this class for image encryption
    """
    __image_key = Random.new().read(AES.block_size)
    __init_vector = Random.new().read(AES.block_size)

    def encrypt_image(self, par_image, par_enc_image):
        """
            this function for encrypting image
            args:
                par_image: the image that is needs to be encrypted
                par_enc_image: an image after encryption
            return:none
        """
        with open(par_image, 'rb') as input_file:
            input_data = input_file.read()
        cfb_cipher = AES.new(self.__image_key, AES.MODE_CFB,
                             self.__init_vector)
        enc_data = cfb_cipher.encrypt(bytearray(input_data))

        with open(par_enc_image, "wb") as enc_file:
            enc_file.write(enc_data)

    def decrypt_image(self, par_enc_image, par_real_image):
        """
        this function for decrypting image
        args:
            par_enc_image: encrypted image
            par_enc_image: the real image
        return:none
        """
        with open(par_enc_image, "rb") as enc_file:
            enc_data = enc_file.read()

        cfb_decipher = AES.new(self.__image_key, AES.MODE_CFB,
                               self.__init_vector)
        plain_data = cfb_decipher.decrypt(enc_data)

        with open("output.jpg", "wb") as output_file:
            output_file.write(plain_data)


class TextEncryption:
    """
        this class for text encryption
        install cryptography.fernet
    """
    __txt_key = Fernet.generate_key()

    def encrypt_text(self, par_txt):
        """
        this function for encrypting text
        args:
            par_txt: text that needs to be encrypted
        return:encrypted text as string
        """
        cipher_suite = Fernet(self.__txt_key)
        return cipher_suite.encrypt(bytes(par_txt, "utf-8"))

    def decrypt_text(self, par_enc_txt):
        """
        this function for decrypting text
        args:
            par_enc_txt: encrypted text
        return:real text
        """
        cipher_suite = Fernet(self.__txt_key)
        return str(cipher_suite.decrypt(par_enc_txt))
