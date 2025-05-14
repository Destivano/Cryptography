# discrete_math_lib/__init__.py
from .number_theory import pow_mod, mod_inverse, euler, gcd, get_divisors
from .prime_operations import (
    get_prime_factors_decomposition, get_distinct_prime_factors,
    is_primitive_root, find_primitive_root,
    second_test_de_Lucas, test_pocklington
)
from .elgamal import generate_elgamal_keys
from .rsa import RSA, RSA_inverse
from .utils import word_to_ascii_list, ascii_list_to_word