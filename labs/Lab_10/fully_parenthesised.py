# Written by Eric Martin for COMP9021


import re

from stack_adt import Stack, EmptyStackError
from binary_tree_adt import BinaryTree


'''
Uses the Stack and BinaryTree interfaces to build an expression tree and evaluate
an arithmetic expression written in infix, fully parenthesised with parentheses,
brackets and braces, and built from natural numbers using the binary +, -, * and / operators.
'''


def parse_tree(expression):
    '''
    Checks whether a expression is a valid fully parentherised infix expression,
    and in case the answer is yes, returns a parse tree for the expression.

    >>> parse_tree('100').print_binary_tree()
    100
    >>> parse_tree('100').evaluate()
    100
    >>> parse_tree('[(1 - 20) + 300]').print_binary_tree()
                1
          -
                20
    +
    <BLANKLINE>
          300
    <BLANKLINE>
    >>> parse_tree('[(1 - 20) + 300]').evaluate()
    281
    >>> parse_tree('( 1 - [ 20 + 300] )').print_binary_tree()
    <BLANKLINE>
          1
    <BLANKLINE>
    -
                20
          +
                300
    >>> parse_tree('( 1 - [ 20 + 300] )').evaluate()
    -319
    >>> parse_tree('{{20*4}/5}').print_binary_tree()
                20
          *
                4
    /
    <BLANKLINE>
          5
    <BLANKLINE>
    >>> parse_tree('{{20*4}/5}').evaluate()
    16.0
    >>> parse_tree('[ 20 * (4 / 5) ]').print_binary_tree()
    <BLANKLINE>
          20
    <BLANKLINE>
    *
                4
          /
                5
    >>> parse_tree('[ 20 * (4 / 5) ]').evaluate()
    16.0
    >>> parse_tree('(1 + {20 * (30 - 400)})').print_binary_tree()
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
          1
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    +
    <BLANKLINE>
                20
    <BLANKLINE>
          *
                      30
                -
                      400
    >>> parse_tree('(1 + {20 * (30 - 400)})').evaluate()
    -7399
    >>> parse_tree('{(1 + 20)*(30 - 400)}').print_binary_tree()
                1
          +
                20
    *
                30
          -
                400
    >>> parse_tree('{(1 + 20)*(30 - 400)}').evaluate()
    -7770
    '''
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = parse_expression(tokens)
        return value
    except ZeroDivisionError:
        return


def parse_expression(tokens):
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for token in tokens:
        try:
            token = BinaryTree(int(token))
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
                parse_tree = BinaryTree(operator)
                parse_tree.left_node = arg_1
                parse_tree.right_node = arg_2
                stack.push(parse_tree)
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    parse_tree = stack.pop()
    if not stack.is_empty():
        return
    return parse_tree


if __name__ == '__main__':
    import doctest
    doctest.testmod()
