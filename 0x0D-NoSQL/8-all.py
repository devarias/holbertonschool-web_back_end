#!/usr/bin/env python3
""" module docs """
import pymongo


def list_all(mongo_collection):
    """ method docs """
    return [p for p in mongo_collection.find()] if mongo_collection else []
