# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:26:34 2018

@author: simha
"""

from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
