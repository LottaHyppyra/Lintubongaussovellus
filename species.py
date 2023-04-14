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