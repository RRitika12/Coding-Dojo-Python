from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def mmf():
    return render_template('checkerboard.html')

@app.route("/<num>") 
def mf(num):
    return render_template('checkerboard2.html',num=int(num))

@app.route("/<num>/<num2>") 
def mf3(num, num2):
    return render_template('checkerboard3.html',num=int(num))


if __name__=="__main__":
    app.run(debug=True)   
