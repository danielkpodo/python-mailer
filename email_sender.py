import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = "Daniel Narh"
email['to'] = "naphthanewman@gmail.com"
email['subject'] = "Good morning is a new day"
email.set_content('You are a python developer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # a way to inform the server u wanna send mail
    smtp.starttls()  # This allow us to connect with the gmail server using tls encryption
    smtp.login("your email address here", "your email password")
    smtp.send_message(email)
    print("Message delivered successfully")
