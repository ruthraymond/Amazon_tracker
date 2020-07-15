import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Samsung-Galaxy-S10-Lite-Hybrid-SIM/dp/B0854FQG6M?smid=A3P5ROKL5A1OLE&pf_rd_r=THZ2DD6V475QEKTDXKRV&pf_rd_p=8d92e357-ed79-4034-8299-ef72c480b787'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError:
        print("Product title: not available")
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])
    
    if (converted_price < 600):
        send_email()

    print(title.strip())
    print(converted_price)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('email.com', 'xxxxxxxxxxxxxx')
    
    subject = 'Priced Reduction on Watched Item!'
    body = 'Check out the Amazon link: https://www.amazon.co.uk/Samsung-Galaxy-S10-Lite-Hybrid-SIM/dp/B0854FQG6M?smid=A3P5ROKL5A1OLE&pf_rd_r=THZ2DD6V475QEKTDXKRV&pf_rd_p=8d92e357-ed79-4034-8299-ef72c480b787'

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'email1@gmail.com',
        'email2@gmail.com',
        msg
    )
    
    print('Message has been sent!')
    server.quit()
    

while(True):
    check_price()    
    time.sleep(86400)