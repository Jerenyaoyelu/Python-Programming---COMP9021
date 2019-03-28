#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:51:41 2018

@author: luyaoye
"""

from math import sqrt


def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


print('The solutions are:\n')
# The list of all even i's such that a + i is one of a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
for a in range(10_001, 100_000 - good_leaps[-1], 2):
    # i should be in good_leaps iff a + i is prime for i = 0, 2, 4, ..., 30.

    #成功了
    #将马丁的一行代码展开：
    for i in range(0, good_leaps[-1] + 1, 2):
        if is_prime(a + i)!=(i in good_leaps):
            break
        if i == good_leaps[-1]:
            for i in good_leaps:
                print(a + i, end = '  ')
            print()
'''
 #报错（没有输出），逻辑应该有问题
    for i in range(0, good_leaps[-1] + 1, 2):
        is_a = True
        if is_prime(a + i)==False:
            break
        elif i not in good_leaps:
            is_a = False
        if i == good_leaps[-1] and is_a == True:
            for i in good_leaps:
                print(a + i, end = '  ')
            print()
'''
    #马丁的方法：
    #如何避免(i in good_leaps)和is_prime(a + i）都为False的情况？(因为(False==False) is True)
    #实际上正是因为这样才避免了，因为若两者都为false或者两者都为true是无法确定a是否为目标序列的开头，
    #而但其中一者为false，一者为true时，表明要么不是质数，要么不满足连续的质数（中间还有其它质数），
    #则可以排除a为目标序列的开头。
    #这个方法相当于把所以不是目标序列开头的a都排除掉了，剩下的就是目标序列了。
    if all(((i in good_leaps) == is_prime(a + i)) for i in range(0, good_leaps[-1] + 1, 2)):
        for i in good_leaps:
            print(a + i, end = '  ')
        print()