from flask import Flask , render_template,request,redirect,url_for
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt',mode='a') as database:
#         email = data['email']
#         name = data['name']
#         comments = data['comments']
#         file = database.write(f'\n{email}, {name}, {comments}')

# def write_to_csv(data):
#     with open('database.csv',mode='a') as database2:
#         email = data['email']
#         name = data['name']
#         comments = data['comments']
#         csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,)
#         csv_writer.writerow([email,name,comments])

def email_sender(data) :
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['From'] = 'server'
    email['To'] = 'erfanshadkam@outlook.com'
    email['Subject'] = 'you have contract'
    email1 = data['email']
    name = data['name']
    comments1 = data['comments']
    email.set_content(html.substitute({'name': email1 , 'email': name, 'comment': comments1}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('emailsenderformywebsite@gmail.com', 'vgnf kefx dkkw yjwv')
        smtp.send_message(email)





@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        email_sender(data)
        return  'thank you i will get in touch with you'
    else:
        return 'something went wrong'





# app.run(host='127.0.0.1',port=8000,debug=True)