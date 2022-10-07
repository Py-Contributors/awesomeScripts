# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This is a sample Python script.

from Encryption import ImageEncryption, TextEncryption

if __name__ == '__main__':
    test_txt = "hello world"
    txt_obj = TextEncryption()
    dec_txt = txt_obj.encrypt_text(test_txt)
    print(dec_txt)
    print(txt_obj.decrypt_text(dec_txt))

    img_obj = ImageEncryption()
    test_image_real_path = "./sunrise.jpg"
    test_image_enc_path = "./encSunrise.jpg"
    test_image_realAfterEnc_path = "./AfterEncSunrise.jpg"
    img_obj.encrypt_image(test_image_real_path, test_image_enc_path)
    img_obj.decrypt_image(test_image_enc_path, test_image_realAfterEnc_path)
