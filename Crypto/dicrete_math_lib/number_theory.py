#Méthode d'exponentiation rapide
def pow_mod(base, exponent, mod):
    result = 1
    base = base % mod  # Update base if it is more than or equal to mod

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if (exponent % 2) == 1:
            result = (result * base) % mod

        # exponent must be even now
        exponent = exponent // 2 # Divide exponent by 2
        base = (base * base) % mod  # Square the base

    return result


def get_divisors(n): # Utilisé par votre is_primitive_root
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


"""
La recherche de l'inverse de a modulo b
"""
#Calculer l'inverse de a modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1


#Trouver le PGCD de deux entiers naturels en utilisant l'algorithme d'Euclide et l'algorithme de la divion continue
def gcd(a, b):
    division = []
    while b:
        division.append(a // b)
        a, b = b, a % b

    return division, a

def division(a, b):
    quotients = gcd(a, b)[0]  # Utiliser gcd(a, b) au lieu de gcd(b, a)
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    for quotient in quotients:
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1

    # x0 est l'inverse de a modulo b si gcd(a, b) == 1
    if (a * x0 + b * y0) == 1:
        return x0 % b  # Assurez-vous que l'inverse est positif
    else:
        return b-x0
    

#Calcul de l'indicatrice d'Euler
def euler(n):
    result = n   # Initialize result as n
    p = 2

    # Check for every number from 2 to sqrt(n)
    while p * p <= n:
        # Check if p is a divisor of n
        if n % p == 0:
            # If yes, then it is a prime factor, subtract multiples of p from result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n

    return result