from flask import Flask
from flask import render_template
import requests

BLOG_API = "https://api.npoint.io/b1aa3a65fe53d4e0e332"

response = requests.get(BLOG_API)



app = Flask(__name__, static_folder='static')
data = response.json()
@app.route("/index.html")
def root():
    return render_template("index.html", text = data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact-me")
def contact_me():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def post(index):
    for item in data:
        if item['id'] == index:
            return render_template('post.html', blog=item)



if __name__ == "__main__":
    app.run(debug=True)