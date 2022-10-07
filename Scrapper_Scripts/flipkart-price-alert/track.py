import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time
from config import MY_EMAIL, RECEIVER_EMAIL, MY_APP_PASSWORD
from config import headers, PRODUCT_URL, THRESHHOLD, CHECK_AGAIN


def sendMail(title):
    '''Send Email'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(MY_EMAIL, MY_APP_PASSWORD)
    subject = 'Change in price detected for ' + title
    print(subject)
    body = 'Click the link to go to the product page ' + PRODUCT_URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(MY_EMAIL, RECEIVER_EMAIL, msg)
    print('Email Sent')
    server.quit()


def priceCheck():
    '''Price checking function'''
    page = requests.get(PRODUCT_URL, headers=headers)
    soup = bs(page.content, 'html.parser')
    # title from _35KyD6 class
    title = soup.find("span", {"class": "_35KyD6"}).get_text()
    # price from '_1vC4OE _3qQ9m1' class,
    # removing unnecessary characters from the price.
    raw_price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
    price = float(raw_price.get_text()[1:].replace(',', ''))
    print(price)
    # If the price falls below threshold, send an email
    if(price < THRESHHOLD):
        sendMail(title)


while(True):
    priceCheck()
    time.sleep(CHECK_AGAIN)
