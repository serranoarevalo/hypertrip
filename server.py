from flask import Flask, render_template, request

app = Flask("hypertrip")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        city = request.form.get('city')
        return render_template("index.html", city=city)


app.run(debug=True)
