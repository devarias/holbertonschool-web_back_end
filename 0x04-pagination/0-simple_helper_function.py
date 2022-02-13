#!/usr/bin/env python3
""" module docs """


def index_range(page, page_size):
    """ method docs """
    if page and page_size:
        start = (page - 1) * page_size
        return start, start + page_size
