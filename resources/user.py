# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:51:33 2018

@author: simha
"""
#import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel




class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="This field cannot be blank.")
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank.")
    
    def post(self):
        
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'Message': "A user with this username already exits."},400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message": "User Created Succesfully."},201
    