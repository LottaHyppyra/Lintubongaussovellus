from app import app
from flask import render_template, request, redirect
import users, sightings, species

@app.route("/")
def index():
    if species.is_empty():
        species.add_species()
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if not users.login(name, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods =["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        name = request.form["name"]

        admin_rights = users.check_if_empty()

        if users.check_name(name):
            return render_template("error.html", message="Käyttäjätunnus varattu")

        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Tunnuksen tulee olla 1-20 merkkiä pitkä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        if not users.register(name, password1, admin_rights):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

        return redirect("/")
    
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        all_species = species.get_names()
        return render_template("add.html", list=all_species)

    if request.method == "POST":
        name = request.form["species"]

        location = request.form["location"]
        if len(location) < 1 or len(location) > 20:
            return render_template("error.html", message="Paikan nimen tulee olla 1-20 merkkiä pitkä.")

        date = request.form["date"]

        sightings.add(name, location, date, users.user_id())
        return redirect("/profile")

app.route("/profile")
def profile():
    if request.method == "GET":
        my_sightings = sightings.get_from_user(users.user_id())
        return render_template("profile.html", list=my_sightings)

@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "GET":
        return render_template("all.html", list=sightings.get_all_by_date())
    
    if request.method == "POST":
        order = request.form["order"]

        if order == "date":
            return render_template("all.html", list=sightings.get_all_by_date())

        if order == "species":
            return render_template("all.html", list=sightings.get_all_by_name())

        if order == "location":
            return render_template("all.html", list=sightings.get_all_by_location())
    
@app.route("/profile")
def profile():
    if request.method == "GET":
        my_sightings = sightings.get_from_user(users.user_id())
        return render_template("profile.html", list=my_sightings)
    
@app.route("/species")
def list_species():
    if request.method == "GET":
        return render_template("species.html", all_species=species.get_all(), len_species=len(species.get_all()), len_families=len(species.get_families()))