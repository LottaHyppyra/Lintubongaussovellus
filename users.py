import os
from flask import abort, request, session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(name, password):
    sql = text("SELECT password, id FROM users WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else: 
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user[1]
            session["user_name"] = name
            return True
    return False

def logout():
    del session["user_id"]
    del session["user_name"]

def register(name, password):
    hash_value = generate_password_hash(password)
    sightings = 0
    try:
        sql = text("INSERT INTO users (name, password, sightings) VALUES (:name, :password, :sightings)")
        db.session.execute(sql, {"name":name, "password":hash_value, "sightings": sightings})
        db.session.commit()
    except:
        return False
    return login(name, password)

def user_id():
    return session.get("user_id", 0)