import os
from dotenv import load_dotenv
import smtplib
from datetime import date
import pandas as pd
import ssl


#function to develop the body of the email with parameters
#when we call this function it is set = email_msg, which fits as a variable in the email message body
#def notification_body(parameters):f'''
#     The world of cypto currency is always changing, keep and eye open for our emails on all the latest changes. 
#     Here are the lowest price exchanges for your prefered coins: {coin1}: {exchange1}, {coin1}: {exchange1}, {coin1}: {exchange1},{coin1}: {exchange1}
#     '''
#     return notificaiton_body

#go into database and get data table of  of email list and coins
#def read_table(engine, 'member_emails_and_coins'):
#     return pd.read_sql_table('member_emails_and_coins', con=engine)
    
# table_dataframe = read_table(engine, 'member_emails_and_coins')

###########################################################################

#demo of email sending message to receiver
def send_email (email_msg):

  #email_msg = notification_body(parameters)
  email_msg = ""f'''
#     The world of cypto currency is always changing, keep and eye open for our emails on all the latest changes. 
#     Here are the lowest price exchanges for your prefered coins: 
#     '''

  email_sender = os.getenv('email_address')
  email_key = os.getenv('email_key')

  #email_receivers = list(pd.read_csv(r".\members_list.csv").loc[:,"emails"].dropna())
  email_receivers = ['artman.jodi@gmail.com'] #+ email_receivers


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

 ##########################

send_email()
