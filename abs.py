# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return (x, [1, 2])
    else:
        return -x
