# Enter you module contents here
"""
    Docstring
"""
from math import sqrt

__author__ = "Nicollas"

__version__ = "1.0"

def hypotenuse(s1, s2):
    """
    Calculates the hypotenuse of a triangle
    """
    return sqrt((s1**2 + s2**2))

def area(s1, s2):
    """Calculates the area of a triangle"""
    return (s1 * s2 * 0.5) 