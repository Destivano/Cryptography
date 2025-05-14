import random
from .number_theory import pow_mod, mod_inverse, gcd, euler 


def RSA(M,n,e):
    #phi_n = euler(n)
    #phi_n
    C = pow_mod(M,e,n)
    return C


def RSA_inverse(C,e,n):
    phi_n=euler(n)

    d = mod_inverse(e, phi_n)
    M = pow_mod(C, d, n)
    return M