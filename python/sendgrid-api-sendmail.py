# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# from address we pass to our Mail object, edit with your name
FROM_EMAIL = 'sac@montesinos.org.es'

# update to your dynamic template id from the UI
TEMPLATE_ID_SPA = 'd-2d30b79433794d8eb9cb60e05d757f0b'
TEMPLATE_ID_CAT = 'd-acc7c0e0f057450fbd6324cc5d60ab5d'

# list of emails and preheader names, update with yours
TO_EMAILS = [('fj.montesinos@gmail.com', 'Javier Montesinos')]

def SendMail():
    idioma = 'spa'
    subject = ''

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS)
    
    if(idioma == 'cat'):
        message.template_id = TEMPLATE_ID_CAT
        subject = 'Registre Actiu'
    else:
        message.template_id = TEMPLATE_ID_SPA
        subject = 'Registro Activo'

    # pass custom values for our HTML placeholders
    message.dynamic_template_data = { 
        'subject': subject,       
        'nombre': 'Manuel'            
    }

    try:        
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)

        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)    


if __name__ == "__main__":
    SendMail()