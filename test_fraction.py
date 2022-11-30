from fraction import Fraction

if __name__ == '__main__':
    # 1
    print(Fraction(1, 2))

    # 2
    print(Fraction(1, 2) + Fraction(2, 3))

    # 3
    print(Fraction(1, 2).invert())

    # 4
    print(Fraction(1, 2).to_float())

    # 5
    print(Fraction(7, 6).integer())

    # 6
    print(Fraction(1, 2) - Fraction(2, 3))
    print(Fraction(1, 2) * Fraction(2, 3))
    print(Fraction(1, 2) / Fraction(2, 3))

    # 7
    print(Fraction(2, 6).simplify())

    # 8
    print(Fraction(1, 2) * 2)

    # 9
    print(Fraction(1, 2) == Fraction(1, 2))
    print(Fraction(1, 2) == Fraction(2, 4))
    print(Fraction(1, 2) == Fraction(1, 4))

    print(f"{Fraction(1, 2)} < {Fraction(1, 4)}:", Fraction(1, 2) < Fraction(1, 4))
    print(f"{Fraction(1, 2)} < {Fraction(2, 4)}:", Fraction(1, 2) < Fraction(2, 4))
    print(f"{Fraction(1, 2)} < {Fraction(3, 4)}:", Fraction(1, 2) < Fraction(3, 4))

    print(f"{Fraction(1, 2)} >= {Fraction(1, 4)}:", Fraction(1, 2) >= Fraction(1, 4))
    print(f"{Fraction(1, 2)} >= {Fraction(2, 4)}:", Fraction(1, 2) >= Fraction(2, 4))
    print(f"{Fraction(1, 2)} >= {Fraction(3, 4)}:", Fraction(1, 2) >= Fraction(3, 4))

    # 11
    print(2 * Fraction(1, 2))

    # 11
    print(Fraction(0.4, 0.2))
