import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = str(input('From: '))
email['To'] = 'erfanshadkam@outlook.com'
email['Subject'] = str(input('Enter subject of the email: '))
email.set_content(html.substitute({'name': name ,'email': email ,'comment': comments }), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('emailsenderformywebsite@gmail.com', 'vgnf kefx dkkw yjwv')
    smtp.send_message(email)
    print('message successfully sent')