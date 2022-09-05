from flask import Flask,render_template,redirect

app=Flask(__name__)
@app.route("/about")
def main():
    return render_template("index.html")

@app.route("/services")
def main1():
    return render_template("services.html")
@app.route("/contact")
def main3():
    return render_template("contact.html")
app.run(debug=True)
