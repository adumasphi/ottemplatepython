#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ottemplatepython example
"""

import Test

if __name__ == '__main__':

    value = 5
    t = Test(value)
    y = t.computeSquared()
    print("The given value is {}.\nThe computed squared value is {}.".format(value, y))

