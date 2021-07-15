# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from address we pass to our Mail object, edit with your name
FROM_EMAIL = 'Servicio de Atención al cliente <sac@montesinos.org.es>'

# list of emails and preheader names, update with yours
TO_EMAILS = 'Javier Montesinos <fj.montesinos@gmail.com>'

MESSAGE_TEMPLAE = """
Dear ${PERSON_NAME}, 

This is a test message. 
Have a great weekend! 

Yours Truly

Javier Montesinos
"""

def SendMail():
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAILS
    msg['Subject'] = 'Sending mails with Python from Sendgrid SMTP Relay'
    mail_body = MESSAGE_TEMPLAE.replace("${PERSON_NAME}", 'Manolo')
    msg.attach(MIMEText(mail_body))

    try:                
        server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)    
        server.login('apikey', os.environ.get('SENDGRID_SMTP_REALY_API_KEY'))
        server.send_message(msg)   

        print("mail sent")
        
    except Exception as e:
        print(e)    


if __name__ == "__main__":
    SendMail()