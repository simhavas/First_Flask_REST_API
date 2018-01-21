# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 07:48:28 2018

@author: simha
"""
import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):
        self.username = username
        self.password = password
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):

        return cls.query.filter_by(username=username).first() #SELECT * FROM users

    @classmethod
    def find_by_id(cls,_id):

        return cls.query.filter_by(id=_id).first()
