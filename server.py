from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def change():
    if request.form["change"] == "add":
        session["count"] += 1
    elif request.form["change"] == "restart":
        session["count"] = 0
    return redirect("/")

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")







if __name__=="__main__":
    app.run(debug=True)