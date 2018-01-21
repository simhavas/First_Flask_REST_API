# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:40:43 2018

@author: simha
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel

                        

def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)