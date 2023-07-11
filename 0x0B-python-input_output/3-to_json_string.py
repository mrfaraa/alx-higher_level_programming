#!/usr/bin/python3
"""
File: 3-to_json_string.py
Desc: This module contains one function;
to_json_string(my_obj)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 11 July 2023
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
