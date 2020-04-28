from flask import Flask, render_template,request
# from random import randint
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('rock.html')

@app.route("/result", methods = ['POST'])
def result():
    print(request.form)
    result = request.form['choice']
#     return render_template('rock.html')
# def randomDigits(digits):
#     lower = 0
#     upper = 2
#     return random.randint(lower, upper)
    return render_template('result.html',result = result)
if __name__ == "__main__":
    app.run(debug=True)