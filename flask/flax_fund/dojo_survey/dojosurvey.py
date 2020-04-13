from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "r1su2lt"

@app.route('/')
def survey():
    return render_template("dojosurvey.html")

@app.route("/result", methods=["POST"])
def survey_result():
    if len(request.form["name"])<1:
        return redirect("/")
    if len(request.form["comments"])<1:
        return redirect("/")
    if len(request.form["comments"])>255:
        return redirect("/")
    else:
        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlanguage = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("surveyresult.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments)


if __name__=="__main__":
    app.run(debug=True) 
