import requests
from bs4 import BeautifulSoup
import smtplib as sl

URL = 'https://www.amazon.de/dp/B081FW6TPQ/ref=sr_1_3?keywords=macbook+pro&qid=1581533259&sr=8-3'

headers = {
    "User-Agent": "Chrome/79.0.3945.130"
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if converted_price < 2.366:
        send_email()

    print(converted_price)
    print(title.strip())

    if converted_price > 2.365:
        send_email()


def send_email():
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email@codixital.com', 'password')

    subject = 'Price down!'
    body = 'Check the following link: https://www.amazon.de/dp/B081FW6TPQ/ref=sr_1_3?keywords=macbook+pro&qid=1581533259&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "codixital@gmail.com",
        "dragus.patrick@icloud.com",
        msg
    )
    print('Email has been send!')

    server.quit()


check_price()
