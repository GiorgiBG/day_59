from flask import Flask
from flask import render_template, request
import requests
from test import SendMail

BLOG_API = "https://api.npoint.io/b1aa3a65fe53d4e0e332"

response = requests.get(BLOG_API)



app = Flask(__name__, static_folder='static')
data = response.json()
@app.route("/")
def root():
    return render_template("index.html", text = data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact-me" )
def contact_me():
    print(request.method)

    return render_template('contact.html')

@app.route("/post/<int:index>")
def post(index):
    for item in data:
        if item['id'] == index:
            return render_template('post.html', blog=item)

@app.route("/form-entry", methods=['POST'])
def receive_data():
    if request.method == "POST":
        send = SendMail(mobile=request.form['mobile'],body=request.form["message"], name=request.form['name'])
        send.send_mail()
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
