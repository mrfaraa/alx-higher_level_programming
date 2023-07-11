#!/usr/bin/python3
"""
File: 4-from_json_string.py
Desc: This module contains one function; from_json_string(my_str)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 11 July 2023
"""

import json


def from_json_string(my_str):
    """
    eturns an object (Python data structure) represented by a
    JSON string
    """
    return json.loads(my_str)
