# Written by Eric Martin for COMP9021


'''
Defines Monomial and Polynomial classes.
A polynomial is built from a string that represents a polynomial, that is,
a sum or difference of monomials.
 - The leading monomial can be either an integer,
   or an integer followed by x,
   or an integer followed by x^ followed by a nonnegative integer.
 - The other monomials can be either a nonnegative integer,
   or a nonnegative integer followed by x,
   or a nonnegative integer followed by x^ followed by a nonnegative integer.
Spaces can be inserted anywhere in the string.
'''


import re


class PolynomialError(Exception):
    def __init__(self, message):
        self.message = message


class Monomial:
    def __init__(self, coefficient = 0, degree = 0):
        self.coefficient = coefficient
        self.degree = degree
        self.next_monomial = None


class Polynomial:
    def __init__(self, input_polynomial):
        '''
        >>> Polynomial('1 2')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('-')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('+0')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('0x^-1')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('2x + +2')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('2x + -2')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> Polynomial('2x - +2')
        Traceback (most recent call last):
        ...
        PolynomialError: Incorrect input
        >>> print(Polynomial('0'))
        0
        >>> print(Polynomial('0x'))
        0
        >>> print(Polynomial('0x^0'))
        0
        >>> print(Polynomial('0x^5'))
        0
        >>> print(Polynomial('x'))
        x
        >>> print(Polynomial('1x'))
        x
        >>> print(Polynomial('1x^1'))
        x
        >>> print(Polynomial('2'))
        2
        >>> print(Polynomial('2x^0'))
        2
        >>> print(Polynomial('1 + 2-3 +10'))
        10
        >>> print(Polynomial('x + x - 2x -3x^1 + 3x'))
        0
        >>> print(Polynomial('x + 2 + x - x -3x^1 + 3x + 5x^0'))
        x + 7
        >>> print(Polynomial('-2x + 7x^3 +x   - 0  + 2 -x^3 + x^23 - 12x^8 + 45 x ^ 6 -x^47'))
        -x^47 + x^23 - 12x^8 + 45x^6 + 6x^3 - x + 2
        '''
        if re.search('\d\s+\d', input_polynomial):
            raise PolynomialError('Incorrect input')
        input_polynomial = input_polynomial.replace(' ', '')
        if not input_polynomial:
            raise PolynomialError('No input')
        if input_polynomial[0] == '+':
            raise PolynomialError('Incorrect input')
        if input_polynomial[0] == '-' and len(input_polynomial) > 1 and input_polynomial[1] == '0':
            raise PolynomialError('Incorrect input')
        if any(input_polynomial[i] in '+-' and not input_polynomial[i - 1].isdigit() and
                                                                      input_polynomial[i - 1] != 'x'
                                                            for i in range(1, len(input_polynomial))
              ):
                raise PolynomialError('Incorrect input')
        input_polynomial = input_polynomial.replace('-', '+-').split('+')
        # For the case where the leading factor is negative.
        if not input_polynomial[0]:
            input_polynomial = input_polynomial[1: ]
        monomial = self._get_monomial(input_polynomial[0])
        if not monomial:
            raise PolynomialError('Incorrect input')
        self.head = monomial
        for input_monomial in input_polynomial[1: ]:
            monomial = self._get_monomial(input_monomial)
            if not monomial:
                raise PolynomialError('Incorrect input')
            if not monomial.coefficient:
                continue
            self._add_monomial(monomial)

    def _get_monomial(self, input_monomial):
        monomial_parts = input_monomial.split('x')
        if len(monomial_parts) > 2:
            return False
        if len(monomial_parts) == 1:
            try:
                coefficient = int(monomial_parts[0])
                return Monomial(coefficient, 0)
            except ValueError:
                return False
        # The case of 'x'.
        if not monomial_parts[0] and not monomial_parts[1]:
            return Monomial(1, 1)
        if not monomial_parts[0]:
            coefficient = 1
        elif monomial_parts[0] == '-':
            coefficient = -1
        else:
            try:
                coefficient = int(monomial_parts[0])
            except ValueError:
                return False
        # Needed for the leading monomial.
        if coefficient == 0:
            degree = 0
        else:
            if not monomial_parts[1]:
                degree = 1
            else:
                if monomial_parts[1][0] != '^':
                    return False
                try:
                    degree = int(monomial_parts[1][1: ])
                    if degree < 0:
                        return False
                except ValueError:
                    return False           
        return Monomial(coefficient, degree)

    def _add_monomial(self, monomial):
        if monomial.degree > self.head.degree:
            monomial.next_monomial = self.head
            self.head = monomial
            return
        if monomial.degree == self.head.degree:
            self._add_monomial_of_same_degree(None, self.head, monomial)
            return              
        node = self.head
        while node.next_monomial and monomial.degree < node.next_monomial.degree:
            node = node.next_monomial
        if not node.next_monomial:
            node.next_monomial = monomial
        elif monomial.degree == node.next_monomial.degree:
            self._add_monomial_of_same_degree(node, node.next_monomial, monomial)
        else:
            monomial.next_monomial = node.next_monomial
            node.next_monomial = monomial
        
    def _add_monomial_of_same_degree(self, parent, node, monomial):
        if node.coefficient + monomial.coefficient:
            node.coefficient += monomial.coefficient
        elif not parent:
            if not self.head.next_monomial:
                self.head = Monomial()
            else:
                self.head = self.head.next_monomial
        else:
            parent.next_monomial = parent.next_monomial.next_monomial
         
    def __str__(self):
        if not self.head:
            return ''
        if not self.head.degree:
            return str(self.head.coefficient)
        if self.head.coefficient == 1:
            output = ''
        elif self.head.coefficient == -1:
            output = '-'
        else:
            output = str(self.head.coefficient)
        output += 'x'
        if self.head.degree > 1:
            output += '^'
            output += str(self.head.degree)
        node = self.head
        while node.next_monomial:
            node = node.next_monomial
            if node.coefficient > 0:
                output += ' + '
            else:
                 output += ' - '
            if abs(node.coefficient) != 1 or node.degree == 0:
                output += str(abs(node.coefficient))
            if node.degree:
                output += 'x'
            if node.degree > 1:               
                output += '^'
                output += str(node.degree)
        return output
                   

if __name__ == '__main__':
    import doctest
    doctest.testmod()
