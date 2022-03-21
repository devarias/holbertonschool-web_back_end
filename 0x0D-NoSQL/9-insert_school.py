#!/usr/bin/env python3
""" module docs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ method docs """
    return mongo_collection.insert_one(kwargs).inserted_id
