from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/visualization")
def visualization():
    return render_template("visualization.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/conclusion")
def conclusion():
    return render_template("conclusion.html")

if __name__ == "__main__":
    app.run(debug=True)