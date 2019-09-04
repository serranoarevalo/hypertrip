from flask import Flask, render_template, request
from hypertrip import hypertrip

app = Flask("hypertrip")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        city = request.form.get('city')
        city_info = hypertrip(city)
        return render_template("index.html", city=city, city_info=city_info)


app.run(debug=True)
