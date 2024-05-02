#!/usr/bin/env python3
""" Pthon script to list all docs in MonogDB """


def list_all(mongo_collection):
    """ List all docs in collection """
    return [doc for doc in mongo_collection.find()]
