import os
from flask import abort, request, session
from sqlalchemy.sql import text
from db import db

def is_empty():
    sql = text("SELECT * FROM species")
    return len(db.session.execute(sql).fetchall()) == 0

def get_all():
    sql = text("SELECT * FROM species")
    return db.session.execute(sql).fetchall()

def get_families():
    sql = text("SELECT * FROM family")
    return db.session.execute(sql).fetchall()

def add_species():
    family = None
    with open("species.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            if parts[0] == "Heimo":
                family = parts[1]
                to_family = text("INSERT INTO family (name) VALUES (:name)")
                db.session.execute(to_family, {"name":family})
                db.session.commit()
                print("lisättiin heimo")
            else:
                name = parts[0]
                latin_name = line.split(")")
                latin_name = latin_name[0].split("(")
                latin_name = latin_name[1]
                print("lisättiin laji")

                try:
                    species = text("INSERT INTO species (latin_name, name, family) VALUES (:latin_name, :name, :family)")
                    db.session.execute(species, {"latin_name":latin_name, "name":name, "family":family})
                    db.session.commit()
                    print("onnistui")

                except:
                    print("ei onnistunut")
                    return False