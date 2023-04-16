from db import db
from sqlalchemy.sql import text

def get_all_by_date():
    sql = text("SELECT species, location, date FROM sightings WHERE visible=TRUE ORDER BY date ASC")
    return db.session.execute(sql).fetchall()

def get_all_by_name():
    sql = text("SELECT species, location, date FROM sightings WHERE visible=TRUE ORDER BY species ASC")
    return db.session.execute(sql).fetchall()

def get_all_by_location():
    sql = text("SELECT species, location, date FROM sightings WHERE visible=TRUE ORDER BY location ASC")
    return db.session.execute(sql).fetchall()

def get_from_user(user_id):
    sql = text("SELECT id, species, location, date FROM sightings WHERE user_id=:user_id AND visible=TRUE ORDER BY date ASC")
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def get_most_common_species():
    sql = text("SELECT species, COUNT(*) amount FROM sightings WHERE visible=TRUE GROUP BY species ORDER BY amount DESC")
    return db.session.execute(sql).fetchone()

def count_all():
    sql = text("SELECT COUNT(*) all FROM sightings WHERE visible=TRUE")
    return db.session.execute(sql).fetchone()

def most_sightings():
    sql = text("SELECT U.name, COUNT(S.species) total FROM Users U LEFT JOIN Sightings S ON U.id=S.user_id WHERE visible=TRUE GROUP BY U.name ORDER BY total DESC")
    return db.session.execute(sql).fetchone()

def add(species, location, date, user_id):
    try:
        sql = text("INSERT INTO sightings (species, location, date, user_id, visible) VALUES (:species, :location, :date, :user_id, :visible)")
        db.session.execute(sql, {"species":species, "location":location, "date":date, "user_id":user_id, "visible":True})
        db.session.commit()
    except:
        return False
    
def delete(sighting_id):
    sql = text("UPDATE sightings SET visible=FALSE WHERE id=:sighting_id")
    db.session.execute(sql, {"sighting_id":sighting_id})
    db.session.commit()
