#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemple class for the python template
"""

__all__ = ['Test', 'myFunction']


class Test():
    """
    Class test

    Parameters
    ----------
    value : float
        The considered value. The considered value.The considered value.
        The considered value.The considered value.The considered value.
        The considered value.
    """
    def __init__(self, value):
        # set attribute
        self.value = value

    def computeSquared(self):
        """
        Method that returns the squared value.

        Returns
        -------
        y : float
            The squared value.
        """
        return self.value**2

    def computeCube(self):
        """
        Method that returns the cube value.

        Returns
        -------
        y : float
            The cube value.
        """
        return self.value**3


def myFunction(arg):
    """
    My particular method

    Parameters
    ----------
    arg : float
    """
    return arg