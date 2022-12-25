

from flask import *
from redis import *
import pickle
app = Flask(__name__)
db = Redis("172.20.0.3", 6379)


@app.route("/")
def redirect_to_login():
    return redirect(url_for("login"))


@app.route("/home", methods=["POST", "GET"],)
def home():
    try:
        if request.method == "POST":
            if "logout" in request.form:
                return redirect(url_for("login"))

        return render_template("home.html", name=request.args["name"], moto=request.args["moto"])
    except:
        return render_template("home.html", name=" user ", moto=" moto ")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["nm"]
        passw = request.form["pass"]
        print(db.get(name))
        print(pickle.loads(db.get(name)))
        if not db.keys(name) == []:
            if pickle.loads(db.get(name))[0] == passw:
                return redirect(url_for("home", name=name, moto=list(pickle.loads(db.get(name)))[1]))
        else:
            pass

        return redirect(url_for("home", name=name, moto=list(pickle.loads(db.get(name)))[1]))
    return render_template("login.html")


@ app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["nm"]
        passw = request.form["pass"]
        moto = request.form["moto"]
        if db.keys(name) == []:
            db.set(name, pickle.dumps([passw, moto]))
            return redirect(url_for("home", name=name, moto=list(pickle.loads(db.get(name)))[1]))
        else:

            pass

    return render_template("register.html")


@ app.route("/home", methods=["POST", "GET"])
def home2():
    if request.method == "POST":
        if "logout" in request.form:
            return redirect(url_for("login"))
    return render_template("home.html", name="user")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
