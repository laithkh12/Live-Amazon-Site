# 🛒 Amazon Price Alert Script

This Python script helps you monitor the price of a product on Amazon and sends an email alert when the price drops below a specified threshold.

## 💡 Description

The script does the following:
1. Scrapes the product page from Amazon to extract the price and title of the product.
2. Compares the product price with a set threshold (`BUY_PRICE`).
3. Sends an email alert if the price is lower than the specified threshold.

## 🧑‍💻 Requirements

Make sure you have the following Python packages installed:

- `beautifulsoup4` (for web scraping)
- `requests` (for making HTTP requests)
- `smtplib` (for sending emails)
- `python-dotenv` (for managing environment variables)

You can install them using pip:

```bash
pip install beautifulsoup4 requests python-dotenv
```
---
## 🔐 Setup
1. Create a .env file:
In your project directory, create a .env file and add your email credentials and SMTP server details:
```bash
SMTP_ADDRESS="smtp.yourmailserver.com"
EMAIL_ADDRESS="your-email@example.com"
EMAIL_PASSWORD="your-email-password"
```
2. Amazon Product URL:
Replace the product URL in the script with the Amazon product you want to monitor.
```python
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
```
3. Set the Buy Price:
Set the threshold price at which you want to be notified. For example, if you want to be alerted when the price drops below $70, set the following:
```python
BUY_PRICE = 70
```
---
## ⚙️ How It Works
1. The script fetches the HTML content of the Amazon product page.
2. It scrapes the product's title and price.
3. The price is compared to the set BUY_PRICE.
4. If the price is lower than the BUY_PRICE, an email is sent to the address specified in your .env file.
---
## 🚀 Usage
1. Clone the repository or copy the code to your local machine.
2. Run the script
3. The script will fetch the product's current price and check if it meets the criteria for sending an alert.
---
## 🛠️ Troubleshooting
- **Email Sending Error**: Ensure your email credentials in the .env file are correct and the SMTP server is accessible.
- **Price Format Error**: If the price scraping fails, make sure the correct CSS classes are used to extract the price from the Amazon product page. The class a- offscreen may change over time.
---
## 📧 Email Format
When the price drops below the threshold, the email sent will look like this:
Subject: Amazon Price Alert!
Message:
"Product Title is on sale for $X.XX!"
[Product URL]
---
## 📝 Notes
- This script works for a specific product on Amazon. If you want to monitor multiple products, you'll need to modify the script accordingly.
- Ensure your email provider allows SMTP connections for sending emails programmatically.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## ⚡ Fun Fact
Did you know? You can automate your shopping with this script and never miss a deal again! 😎
