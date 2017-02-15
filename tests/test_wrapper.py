from __future__ import print_function
from ottemplatepython import Test


def test_squared():
    t = Test(3)
    x = t.computeSquared()
    assert x == 9, 'Values do not match'
