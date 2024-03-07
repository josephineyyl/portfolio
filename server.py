from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def workhtml_pages(page_name=None):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Error saving to database!!'
    else:
        return "something wrong"

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
    with open('database.csv', 'a') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        
        #testing