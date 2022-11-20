import os
from dotenv import load_dotenv
import smtplib
from datetime import date

def send_email():
    load_dotenv()
    sender_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_KEY')

    receiver_address = ['artman.jodi@gmail.com'] #+ ['firas.obied@lau.edu'] + email_list

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_address, email_password)

        current_date = date.today()
        current_date = current_date.strftime("%m/%d/%Y")

        subject = f'Crypto Updade for {current_date}'
        body = f"""\n
        Hello, 
        The world of cypto currency is always changing, keep and eye open for our emails on all the latest changes. 
        Here are the lowest price exchanges for your prefered coins:
        <function to grab from database and current data not yet written>

        Your Crypto Team,
        BCS Rocks"""
        msg = f'subject: {subject}\n\n{body}'

        smtp.sendmail(sender_address, receiver_address, msg)

send_email()  