from sqlalchemy.sql import text
from db import db

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
            else:
                name = parts[0]
                latin_name = line.split(")")
                latin_name = latin_name[0].split("(")
                latin_name = latin_name[1]

                try:
                    specie = text("INSERT INTO species (latin_name, name, family_id) VALUES (:latin_name, :name, :family_id)")
                    db.session.execute(specie, {"latin_name":latin_name, "name":name, "family":family})
                    db.session.commit()

                except:
                    return False
                
if __name__ == "__main__":
    add_species()