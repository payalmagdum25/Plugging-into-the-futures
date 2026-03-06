from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    tableau_url = "https://public.tableau.com/shared/6Y82R5CQT?:display_count=n&:origin=viz_share_link"
    return render_template("index.html", tableau_url=tableau_url)

if __name__ == "__main__":
    app.run(debug=True)