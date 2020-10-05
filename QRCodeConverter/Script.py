import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  

def QRCodeConverter(url, count):

    qr = pyqrcode.create(url) # Generating the QR code
    qr.png(f'./QRCodeConverter/QRCode-{count}.png', scale = 6) # Saving the QR code as a PNG
    print("QR Code saved!")

choice = 'y'
count = 0
while(choice == 'y' or choice == 'yes'):
    count = count + 1
    url = input("Enter the URL to convert into a QR Code: ")
    QRCodeConverter(url, count)
    choice = input('Do you want to convert another URL? (y/yes for yes, any other key for no): ')
    
