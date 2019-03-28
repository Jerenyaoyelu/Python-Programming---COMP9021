# Written by Eric Martin for COMP9021



'''
Uses the stack_adt module to evaluate an arithmetic expression
written in infix, fully parenthesised with parentheses, brackets and braces,
and built from natural numbers using the binary +, -, * and / operators.
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):
    '''
    Checks whether an expression is a valid fully parentherised infix expression,
    and in case the answer is yes, returns the value of the expression,
    provided that no division by 0 is attempted; otherwise, return None.

    >>> evaluate('100')
    100
    >>> evaluate('[(1 - 20) + 300]')
    281
    >>> evaluate('[1 - {20 + 300}]')
    -319
    >>> evaluate('( { 20*4 }/5 )')
    16.0
    >>> evaluate('(20*[4/5])')
    16.0
    >>> evaluate('({1 + (20 * 30)} - [400 / 500])')
    600.2
    >>> evaluate('{1 + [((20*30)-400) / 500]}')
    1.4
    >>> evaluate('[1 + {(2 * (3+{4*5})) / ([6*7]-[8/9]) }]')
    2.1189189189189186
    >>> evaluate('100 + 3')
    >>> evaluate('(100 + 3')
    >>> evaluate('(100 + -3)')
    >>> evaluate('(100 \ 50)')
    >>> evaluate('(100 / 0)')    
    '''
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return


def evaluate_expression(tokens):
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for token in tokens:
        try:
            token = int(token)
        except ValueError:
            pass
        if token not in parentheses:
            stack.push(token)
        else:
            try:
                arg_2 = stack.pop()
                operator = stack.pop()
                arg_1 = stack.pop()
                opening_group_symbol = stack.pop()
                if parentheses[token] != opening_group_symbol:
                    return
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[operator](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
