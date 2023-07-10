#!/usr/bin/python3
"""
File: 4-inherits_from.py
Desc: This module contains one function;
inherits_from(obj, a_class)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 10 July 2023
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited from(directly or indirectly), the specified class;
    otherwise
    False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
