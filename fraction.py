def gcd(a, b):
    """
    Compute the greatest common divider of a and b in a recursive manner.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


class Fraction(object):
    """
    A simple fraction class.
    """

    def __init__(self, numerator, denominator=1):
        """
        Creates a new fraction.
        """
        if isinstance(numerator, int) and isinstance(denominator, int):
            self._numerator = numerator
            self._denominator = denominator
        else:
            raise ValueError("Expecting integers.")

    # 1. Add a member function to give a print representation for the class,
    #    e.g., `print(Fraction(1, 2))` should yield in something like: `1/2`.
    def __str__(self):
        return str(self._numerator) + "/" + str(self._denominator)

    # 2. Add a member function to add to fractions,
    #    e.g., `print(Fraction(1, 2)+ Fraction(2, 3))` should yield `7/6`.
    #    Remember: the return type should be chosen correctly, e.g., the
    #    addition of two fractions results in a new fraction, not a string
    #    representation of the result!
    def __add__(self, other):
        return Fraction(
            self._numerator * other._denominator + other._numerator * self._denominator,
            self._denominator * other._denominator,
        )

    # 3. Add a member function to invert a fraction, e.g.,
    #   `print(Fraction(1, 2).invert())` should yield `2/1`.
    def invert(self):
        return Fraction(self._denominator, self._numerator)

    # 4. Add a member function to give a decimal representation of a fraction,
    #    e.g., `print(Fraction(1, 2).to_float())` should yield `0.5`.
    def to_float(self):
        return self._numerator / self._denominator

    # 5. Add a member function that returns the *integer part* of a fraction,
    #    e.g., `Fraction(7, 6).integer()` should yield `1`.
    def integer(self):
        return self._numerator // self._denominator

    # 6. Add member functions to subtract, multiply and divide fractions.
    #    Hint: can we reuse any of the member functions?
    def __sub__(self, other):
        return Fraction(
            self._numerator * other._denominator - other._numerator * self._denominator,
            self._denominator * other._denominator,
        )

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self._numerator * other._numerator,
                self._denominator * other._denominator,
            )
        # 11. Can you add integer multiplication functionality, e.g.,
        #     print(Fraction(1, 2) * 2) should yield 2/2.
        elif isinstance(other, int):
            return Fraction(self._numerator * other, self._denominator)

    def __truediv__(self, other):
        return self * other.invert()

    # 7. Add a member function to simplify a fraction,
    #    e.g., `print(Fraction(2, 6).simplify())` should yield `1/3`.
    #    Hint: use a function to calculate the greatest common divisor.
    def simplify(self):
        divisor = gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // divisor
        self._denominator = self._denominator // divisor
        return self

    # 9. Add some comparison operators, e.g., == and <.
    def __eq__(self, other):
        s_s = Fraction(self._numerator, self._denominator).simplify()
        s_o = Fraction(other._numerator, other._denominator).simplify()
        return s_s._denominator == s_o._denominator and s_s._numerator == s_o._numerator

    def __lt__(self, other):
        # return self.to_float() >= other.to_float()
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __ge__(self, other):
        # return self.to_float() >= other.to_float()
        return self._numerator * other._denominator >= other._numerator * self._denominator

    # 11. What about commutativity?
    def __rmul__(self, other):
        if isinstance(other, int):
            return Fraction(self._numerator * other, self._denominator)
