#!/usr/bin/env python3
""" module docs """
import pymongo


def top_students(mongo_collection):
    """ method docs """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
