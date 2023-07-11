#!/usr/bin/python3
"""
File: 8-class_to_json.py
Desc: This module contains one function; class_to_json(obj)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 11 July 2023
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    return obj.__dict__
