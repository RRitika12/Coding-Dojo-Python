from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/play')  
def play():
    return render_template('playg.html') 

@app.route('/play/<num>') 
def block_repeat(num):       
    return render_template('playg2.html', repeat=int(num))

@app.route('/play/<num>/<colorChange>')
def box_color(num,colorChange):
    return render_template('playg3.html', repeat=int(num), colorChange = colorChange )

if __name__=="__main__":
    app.run(debug=True)             


