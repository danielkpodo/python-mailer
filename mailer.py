import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Path functions like os.path to enable us grab the path of the index.html
# Template allows us to inject words into our html

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Daniel Narh'
email['to'] = 'vatinyo@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
# To read the mail as an html format set pass the format to the substitute
# The name key is what is going to be substituted in the html
# The substitute can be keyword args or as a dictionary
email.set_content(html.substitute({'name': 'Victronix'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # a way to inform the server u wanna send mail
    smtp.starttls()  # This allow us to connect with the gmail server using tls encryption
    smtp.login('<your email address>', '<your password here>')
    smtp.send_message(email)
    print('Message Delivered')
