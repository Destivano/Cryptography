import random 
from .number_theory import pow_mod, mod_inverse, gcd



"""
ElGamal Encryption and Decryption
clé privée : a tel que 1< a < p
clé publique : (A, g, p) tel que A = g^a mod p,  g racine primitive modulo p

Encryption:
To encrypt a message M:
Choose a random integer b such that b coprime to p-1.
Compute B = g^b mod  p.
Compute C = M⋅A^b mod  p.
The ciphertext is (B, C).

Decryption:
To decrypt the ciphertext (B, C):
Compute M = C ⋅ B^(p-a-1) mod p.
"""

# Generating b
def generate_elgamal_keys(q):
    key = random.randint(1, q-1)
    while gcd(-1, key)[1] != 1:
        key = random.randint(1, q-1)

    return key


def générer_BC(g,p,A,asc):
    return pow_mod(g, generate_elgamal_keys(p-1), p), ((pow_mod(A, generate_elgamal_keys(p-1), p)) * asc) % p