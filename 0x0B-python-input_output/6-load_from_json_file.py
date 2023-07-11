#!/usr/bin/python3
"""
File: 6-load_from_json_file.py
Desc: This module contains one function; load_from_json_file(filename)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 11 July 2023
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, "r") as f:
        return json.load(f)
