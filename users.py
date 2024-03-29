import os
from flask import abort, request, session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(name, password):
    sql = text("SELECT password, id, admin_rights FROM users WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else: 
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user[1]
            session["user_name"] = name
            session["user_admin_rights"] = user[2]
            return True
    return False

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_admin_rights"]

def register(name, password, admin_rights):
    hash_value = generate_password_hash(password)
    sightings = 0
    try:
        sql = text("INSERT INTO users (name, password, admin_rights, sightings) VALUES (:name, :password, :admin_rights, :sightings)")
        db.session.execute(sql, {"name":name, "password":hash_value, "admin_rights": admin_rights, "sightings": sightings})
        db.session.commit()
    except:
        return False
    return login(name, password)

#return TRUE when username is taken
def check_name(name):
    sql = text("SELECT name FROM users WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    account = result.fetchone()
    if not account:
        return False
    return True

#return TRUE if users is empty
def check_if_empty():
    sql = text("SELECT * FROM users")
    result = db.session.execute(sql)
    accounts = len(result.fetchall())
    return accounts == 0

def get_normal_accounts():
    admin_rights = False
    sql = text("SELECT id, name FROM users WHERE admin_rights=:admin_rights")
    return db.session.execute(sql, {"admin_rights":admin_rights}).fetchall()

def give_admin_rights(user_id):
    sql = text("UPDATE users SET admin_rights=TRUE WHERE id=:user_id")
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()

def user_id():
    return session.get("user_id", 0)

def add_follow(species, user_id):
    try:
        sql = text("INSERT INTO followed_species (user_id, species) VALUES (:user_id, :species) ON CONFLICT DO NOTHING")
        db.session.execute(sql, {"user_id":user_id, "species":species})
        db.session.commit()
    except:
        return False
    
def get_follows_from_user(user_id):
    sql = text("SELECT species FROM followed_species WHERE user_id=:user_id")
    return db.session.execute(sql, {"user_id":user_id}).fetchall()