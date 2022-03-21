#!/usr/bin/env python3
""" module docs """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ method docs """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
