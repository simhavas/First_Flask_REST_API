# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:35:31 2018

@author: simha
"""
#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("Price",type=float,required=True,help="This field cannot be left blank!")
    #data = request.get_json()
    parser.add_argument("store_id",type=int,required=True,help="Every item neds a store id.")
        
    @jwt_required()
    def get(self,name):
        
        item = ItemModel.find_by_name(name)
        if item: 
            return item.json()
        
        return {'message': 'Item not found.'},404
      

    
    def post(self,name):
#        parser = reqparse.RequestParser()
#        parser.add_argument("Price",type=float,required=True,help="This field cannot be left blank!")
        #data = request.get_json()
        
        #item1 = next(list(filter(lambda x: x["name"] == name, items)).__iter__(), None)
        item1 = ItemModel.find_by_name(name)
        if item1:
            return ({"message": "An item with name {} already exists.".format(name)}, 400)
        #data = request.get_json(silent=True)
        data = Item.parser.parse_args()
        item = ItemModel(name,**data)
        
        try:
            item.save_to_db() 
        except:
            return {"message": "An error occured inserting the item."},500 # Internal Server error
        
        return item.json(), 201
    
    
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': 'Item deleted'}
    
    def put(self,name):
        #parser = reqparse.RequestParser()
        #parser.add_argument("Price",type=float,required=True,help="This field cannot be left blank!")
        #data = request.get_json()
        data = Item.parser.parse_args()
        #item = next(list(filter(lambda x: x["name"] == name, items)).__iter__(), None)
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name,data['Price'],data['store_id'])     
        else:
           item.Price = data['Price']
           item.store_id = data['store_id']
           
        item.save_to_db()
           
        return item.json()
    
  
    
    
class ItemList(Resource):
    def get(self):
        
        #return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
