# Written by Eric Martin for COMP9021


'''
Defines Monomial and Polynomial classes.
A polynomial is built from a string that represents a polynomial,
that is, a sum or difference of monomials.
- The leading monomial can be either an integer,
  or an integer followed by x,
  or an integer followed by x\^ followed by a nonnegative integer.
- The other monomials can be either a nonnegative integer,
  or an integer followed by x,
  or an integer followed by x\^ followed by a nonnegative integer.
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
    def __init__(self, input_polynomial = None):
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
        if input_polynomial is None:
            self.head = None
            return
        if re.search('\d\s+\d', input_polynomial):
            raise PolynomialError('Incorrect input')
        input_polynomial = input_polynomial.replace(' ', '')
        if not input_polynomial:
            raise PolynomialError('No input')
        if input_polynomial[0] == '+':
            raise PolynomialError('Incorrect input')
        if input_polynomial[0] == '-' and len(input_polynomial) > 1 and input_polynomial[1] == '0':
            raise PolynomialError('Incorrect input')
        for i in range(1, len(input_polynomial)):
            if (input_polynomial[i] in '+-' and
                not input_polynomial[i - 1].isdigit() and
                input_polynomial[i - 1] != 'x'):
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

    def _copy(self):
        copy = Polynomial()
        if not self.head:
            return copy
        copy.head = Monomial(self.head.coefficient, self.head.degree)
        node = self.head.next_monomial
        node_copy = copy.head
        while node:
            node_copy.next_monomial = Monomial(node.coefficient, node.degree)
            node = node.next_monomial
            node_copy = node_copy.next_monomial
        return copy
            
    def _get_monomial(self, input_monomial):
        monomial_parts = input_monomial.split('x')
        if len(monomial_parts) > 2:
            return False
        if len(monomial_parts) == 1:
            try:
                coefficient = int(monomial_parts[0])
                return Monomial(coefficient, 0)
            except:
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
            except:
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
                except:
                    return False           
        return Monomial(coefficient, degree)

    def _add_monomial(self, monomial):
        if not self.head:
            self.head = monomial
            return
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

    def _multiply_monomial(self, monomial):
        if not monomial.coefficient:
            self.head.coefficient = 0
            self.head.degree = 1
            self.head.next_monomial = None
            return
        node = self.head
        while node:
            node.coefficient *= monomial.coefficient
            node.degree += monomial.degree
            node = node.next_monomial
         
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
                   
    def __add__(self, polynomial):
        '''
        >>> poly_1 = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> poly_2 = Polynomial('192 -71x^3 + 8x^2 + 2x^5 -6x - 93x^4')
        >>> print(poly_1 + poly_2)
        4x^5 - 186x^4 - 142x^3 + 16x^2 - 12x + 384
        >>> print(poly_1)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        >>> print(poly_2)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        '''
        copy = self._copy()
        node = polynomial.head
        while node:
            copy._add_monomial(Monomial(node.coefficient, node.degree))
            node = node.next_monomial
        return copy

    def __mul__(self, polynomial):
        '''
        >>> poly = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> print(poly * poly)
        4x^10 - 372x^9 + 8365x^8 + 13238x^7 + 3529x^6 + 748x^5 - 34796x^4 - 27360x^3 + 3108x^2 \
- 2304x + 36864
        >>> print(poly)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        >>> poly_1 = Polynomial('-11x^4 + 3x^2 + 7x + 9')
        >>> poly_2 = Polynomial('5x^2 -8x - 6')
        >>> print(poly_1 * poly_2)
        -55x^6 + 88x^5 + 81x^4 + 11x^3 - 29x^2 - 114x - 54
        >>> print(poly_1)
        -11x^4 + 3x^2 + 7x + 9
        >>> print(poly_2)
        5x^2 - 8x - 6
        >>> poly_1 = Polynomial('-2x + 7x^3 +x   - 0  + 2 -x^3 + x^23 - 12x^8 + 45 x ^ 6 -x^47')
        >>> poly_2 = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> print(poly_1 * poly_2)
        -2x^52 + 93x^51 + 71x^50 - 8x^49 + 6x^48 - 192x^47 + 2x^28 - 93x^27 - 71x^26 + 8x^25 - 6x^24 \
+ 192x^23 - 24x^13 + 1116x^12 + 942x^11 - 4281x^10 - 3123x^9 - 1932x^8 - 828x^7 + 8212x^6 + 145x^5 \
- 151x^4 + 1002x^3 + 22x^2 - 204x + 384
        >>> print(poly_1)
        -x^47 + x^23 - 12x^8 + 45x^6 + 6x^3 - x + 2
        >>> print(poly_2)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        '''
        product = Polynomial()
        node = polynomial.head
        while node:
            product_by_monomial = self._copy()
            product_by_monomial._multiply_monomial(Monomial(node.coefficient, node.degree))
            second_node = product_by_monomial.head
            while second_node:
                product._add_monomial(Monomial(second_node.coefficient, second_node.degree))
                second_node = second_node.next_monomial
            node = node.next_monomial
        return product

    def __sub__(self, polynomial):
        '''
        >>> poly = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> print(poly - poly)
        0
        >>> print(poly) 
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        '''
        return self.__add__(polynomial.__mul__(Polynomial('-1')))

    def __truediv__(self, polynomial):
        '''
        >>> poly_1 = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> poly_2 = Polynomial('4x^5 - 186x^4 - 142x^3 + 16x^2 - 12x + 384')
        >>> print(poly_1 / poly_2)
        None
        >>> print(poly_1)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        >>> print(poly_2)
        4x^5 - 186x^4 - 142x^3 + 16x^2 - 12x + 384
        >>> poly_1 = Polynomial('-55x^6 + 88x^5 + 81x^4 + 11x^3 - 29x^2 - 114x - 54')
        >>> poly_2 = Polynomial('-11x^4 + 3x^2 + 7x + 9')
        >>> poly_3 = Polynomial('5x^2 -8x - 6')
        >>> print(poly_1 / poly_2)
        5x^2 - 8x - 6
        >>> print(poly_1 / poly_3)
        -11x^4 + 3x^2 + 7x + 9
        >>> print(poly_1)
        -55x^6 + 88x^5 + 81x^4 + 11x^3 - 29x^2 - 114x - 54
        >>> print(poly_2)
        -11x^4 + 3x^2 + 7x + 9
        >>> poly_1 = Polynomial('-2x + 7x^3 +x   - 0  + 2 -x^3 + x^23 - 12x^8 + 45 x ^ 6 -x^47')
        >>> poly_2 = Polynomial('2x^5 - 71x^3 + 8x^2 - 93x^4 -6x + 192')
        >>> poly_1 = Polynomial('-2x^52 + 93x^51 + 71x^50 - 8x^49 + 6x^48 - 192x^47 + 2x^28 - 93x^27 - \
71x^26 + 8x^25 - 6x^24 + 192x^23 - 24x^13 + 1116x^12 + 942x^11 - 4281x^10 - 3123x^9 - 1932x^8 - 828x^7 \
+ 8212x^6 + 145x^5 - 151x^4 + 1002x^3 + 22x^2 - 204x + 384')
        >>> poly_2 = Polynomial('-x^47 + x^23 - 12x^8 + 45x^6 + 6x^3 - x + 2')
        >>> poly_3 = Polynomial('2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192')
        >>> print(poly_1 / poly_2)
        2x^5 - 93x^4 - 71x^3 + 8x^2 - 6x + 192
        >>> print(poly_1 / poly_3)
        -x^47 + x^23 - 12x^8 + 45x^6 + 6x^3 - x + 2
        '''
        quotient = Polynomial()
        copy = self._copy()
        while copy.head.coefficient and copy.head.degree:
            if copy.head.coefficient % polynomial.head.coefficient:
                return
            if copy.head.degree < polynomial.head.degree:
                return
            polynomial_copy = polynomial._copy()
            coefficient = copy.head.coefficient // polynomial.head.coefficient
            degree = copy.head.degree - polynomial.head.degree
            polynomial_copy._multiply_monomial(Monomial(-coefficient, degree))
            copy = copy.__add__(polynomial_copy)
            quotient._add_monomial(Monomial(coefficient, degree))                                     
        return quotient


if __name__ == '__main__':
    import doctest
    doctest.testmod()        

