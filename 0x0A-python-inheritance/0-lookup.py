#!/usr/bin/python3
"""
File: 0-lookup.py
Desc: This module contains one function; lookup(obj)
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 10 July 2023
"""


def lookup(obj):
    """
    Returns the list of available attributes and
    methods of an object
    """
    return dir(obj)
