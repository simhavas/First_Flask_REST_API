# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 07:55:47 2018

@author: simha
"""

#import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    Price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    
    
    def __init__(self,name,Price,store_id):
        self.name = name
        self.Price = Price
        
    def json(self):
        return {'name': self.name, 'Price': self.Price}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1
        
   
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
        
   
    def delete_from_db(self):
      db.session.delete(self)
      db.session.commit()