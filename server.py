
from flask import Flask , render_template,request,redirect,url_for
import csv
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

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email = data['email']
        name = data['name']
        comments = data['comments']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,)
        csv_writer.writerow([email,name,comments])




@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return  'thank you i will get in touch with you'
    else:
        return 'something went wrong'


#sdas


app.run(host='127.0.0.1',port=8000,debug=True)