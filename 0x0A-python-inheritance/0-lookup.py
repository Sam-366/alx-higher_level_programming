#!/usr/bin/python3
"""This Defines an object attribute lookup function."""

def lookup(obj):
    """This Returns a list of an object's available attributes."""
    return (dir(obj))
