import os
from dotenv import load_dotenv
import smtplib
from datetime import date
import pandas as pd
import ssl

print(load_dotenv())

email_sender = os.getenv('email_address')
email_key = os.getenv('email_key')

#email_receivers = list(pd.read_csv(r".\members_list.csv").loc[:,"emails"].dropna())
email_receivers = ['theartman4@gmail.com'] #+ email_receivers

global email_msg

current_date = date.today()
current_date = current_date.strftime("%d/%m/%Y")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_sender, email_key)
    
    subject = f'Crypto Updade for {current_date}'
    email_body = f"""\
    Hello, 
    {email_msg}

    Yours Crypto Team,
    BCS Rocks"""
    msg = f'Subject: {subject}\n\n{email_body}'
    smtp.sendmail(email_sender, email_receivers, msg)
    
print('sweet baby jeasus this worked')


