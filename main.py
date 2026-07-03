import time
from email.message import EmailMessage
import smtplib
import requests
import schedule

API_KEY = "cur_live_DL9YXAs9IozYLtQtUnNCuMqSiOXLtmqZfg0ijVMu"

SENDER_EMAIL = "o1719933580@gmail.com"
SENDER_PASSWORD = "zfpvkxoevpcnmtmw"
RECEIVER_EMAIL = "yeashtarunawork@gmail.com"

def scrape_conversion():
    api_url = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}&base_currency=USD"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        bdt_rate = data["data"]["BDT"]["value"]
        return bdt_rate
    else:
        return None
    
def send_mail(conversion):
    msg = EmailMessage()
    msg["Subject"] = "Official Daily Currency Exchange Rate Notification"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    email_body = (
        "Hello,\n\n"
        "This is your official daily notification regarding the current foreign exchange rates.\n\n"
        "Please find the verified currency conversion details for today below:\n\n"
        f"Base Currency: 1.00 USD (United States Dollar)\n"
        f"Exchange Rate: {conversion:.2f} BDT (Bangladeshi Taka)\n\n"
        "All figures are processed directly through real-time financial market data.\n\n"
        "Best regards,\n"
        "Currency Administration System"
    )

    msg.set_content(email_body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()


def temp_alart_system():
    conversion = scrape_conversion()
    if conversion:
        send_mail(conversion)
    else:
        print("Server error")

schedule.every().day.at("19:25").do(temp_alart_system)

while True:
    schedule.run_pending()
    time.sleep(1)