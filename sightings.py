from db import db
from sqlalchemy.sql import text

def get_all_by_date():
    sql = text("SELECT species, location, date FROM sightings ORDER BY date ASC")
    return db.session.execute(sql).fetchall()

def get_all_by_name():
    sql = text("SELECT species, location, date FROM sightings ORDER BY species ASC")
    return db.session.execute(sql).fetchall()

def get_all_by_location():
    sql = text("SELECT species, location, date FROM sightings ORDER BY location ASC")
    return db.session.execute(sql).fetchall()

def get_from_user(user_id):
    sql = text("SELECT species, location, date FROM sightings WHERE user_id=:user_id ORDER BY date ASC")
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def get_most_common_species():
    sql = text("SELECT species, COUNT(*) amount FROM sightings GROUP BY species ORDER BY amount DESC")
    return db.session.execute(sql).fetchone()

def count_all():
    sql = text("SELECT COUNT(*) all FROM sightings")
    return db.session.execute(sql).fetchone()

def add(species, location, date, user_id):
    try:
        sql = text("INSERT INTO sightings (species, location, date, user_id) VALUES (:species, :location, :date, :user_id)")
        db.session.execute(sql, {"species":species, "location":location, "date":date, "user_id":user_id})
        db.session.commit()
    except:
        return False