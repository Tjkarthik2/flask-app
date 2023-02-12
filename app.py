from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/test", methods=['GET'])
def nextPage():
    return render_template("next_page.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)