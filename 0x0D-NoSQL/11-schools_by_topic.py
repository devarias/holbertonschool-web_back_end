#!/usr/bin/env python3
""" module docs """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ method docs """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
