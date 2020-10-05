import pyqrcode
# import png
# from pyqrcode import QRCode


def QRCodeConverter(url, count):
    qr = pyqrcode.create(url)  # Generating the QR code
    # Saving the QR code as a PNG
    qr.png(f'./QRCodeConverter/QRCode-{count}.png', scale=6)
    print("QR Code saved!")


choice = 'y'
count = 0
while(choice == 'y' or choice == 'yes'):
    count = count + 1
    url = input("Enter the URL to convert into a QR Code: ")
    QRCodeConverter(url, count)
    print('Do you want to convert another URL?')
    choice = input('(y/yes for yes, any other key for no): ')
