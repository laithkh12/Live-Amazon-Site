from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

BUY_PRICE = 70

load_dotenv()


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

productPrice = soup.find(class_="a-offscreen").get_text()

priceWithoutCurrency = productPrice.split("$")[1]

priceAsFloat = float(priceWithoutCurrency)
print(priceAsFloat)

productTitle = soup.find(id="productTitle").get_text().strip()
print(productTitle)



if priceAsFloat < BUY_PRICE:
    message = f"{productTitle} is on sale for {productPrice}!"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )