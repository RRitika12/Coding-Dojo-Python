from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "wheremygold@"


@app.route("/")
def gold_count_start():

    if "gold_count" not in session:
        session["gold_count"] = 0
    if "act_log" not in session:
        print("We ain't found shit")
        session["act_log"] = []
    act_log = session["act_log"]
    gold_count = session["gold_count"]
    return render_template("ninja_gold.html", act_log = act_log, gold_count = gold_count)

@app.route("/process_money", methods=["POST"])
def get_gold():
    
    if request.form["button"] == "farm":
        num = random.randrange(1,3)
        if num == 1:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'> you've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session.modified = True
            session["gold_count"] += goldval
        if num == 2:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> You lost %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    
    if request.form["button"] == "cave":
        num = random.randrange(1,3)
        if num == 1:
            goldval = random.randrange(0,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'> You've earned %s gold!  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if num == 2:
            goldval = random.randrange(1,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you lost %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "house":
        num = random.randrange(1,3)
        if num == 1:
            goldval = random.randrange(2,6)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Earned %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if num == 2:
            goldval = random.randrange(2,5)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> You lost %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "casino":
        num = random.randrange(1,3)
        if num == 1:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Earned %s gold from the casino! (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        
        if num == 2:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you've lost %s gold from the casino! (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    return redirect("/")

@app.route("/restart")
def reset_game():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True) 
