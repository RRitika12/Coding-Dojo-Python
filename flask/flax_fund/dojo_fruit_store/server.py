from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    now=datetime.datetime.now()
    timestamp=now.strftime("%B %d %Y %I:%M %p")
    print(request.form)
    return render_template("checkout.html", timestamp=timestamp)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    