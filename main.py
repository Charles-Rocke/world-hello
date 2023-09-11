from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdfghjkl"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return "<h2>About page</h2>"


# running the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
