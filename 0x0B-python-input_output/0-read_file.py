#!/usr/bin/python3
"""
File: 0-read_file.py
Desc: This module contains one function; read_file(filename="")
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 11 July 2023
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
