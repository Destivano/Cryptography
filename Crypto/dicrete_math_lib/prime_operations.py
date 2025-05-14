from .number_theory import pow_mod, get_divisors

#Générer tous les facteurs premiers d'un entier naturel en utilisant la méthode du Sieve d'Ératosthène
def get_prime_factors_decomposition(n):
    limit = n
    prime = [True for i in range(limit + 1)]
    p = 2
    while (p * p <= limit):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, limit + 1) if prime[p]]

    # Perform prime factorization
    decomposition = {}
    for prime in primes:
        while n % prime == 0:
            if prime in decomposition:
                decomposition[prime] += 1
            else:
                decomposition[prime] = 1
            n //= prime
        if n == 1:
            break

    return decomposition



def get_distinct_prime_factors(n):
     return list(get_prime_factors_decomposition(n).keys())


def is_primitive_root(g, p):
    phi = p - 1
    #divisors = get_divisors(phi)
    #condition= True
    for e in range(1, phi):
        if pow_mod(g, e, p) == 1:
            return False
        
    if pow_mod(g, phi, p) != 1:
        return False
    
    return True


def find_primitive_root(p):
    racines = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            racines.append(g)
    return racines if racines else None


def second_test_de_Lucas(n): # Renommer pour refléter l'utilisation : is_prime_lucas_variant
    bases=[2,3,5,7,11,13,17,19,23,29] # Ou des bases aléatoires
    if n < 2: return False
    if n == 2: return True # 2 est premier
    if n % 2 == 0: return False # Si pair et > 2, non premier

    # Pré-calcul des facteurs premiers de n-1
    phi = n - 1
    prime_factors_phi = get_distinct_prime_factors(phi)
    if not prime_factors_phi and phi > 1: # n-1 est premier
        prime_factors_phi = [phi]
    elif not prime_factors_phi and phi == 1: # n=2
         pass # Déjà géré

    for base in bases:
        if base >= n: continue
        if pow_mod(base, phi, n) != 1: # Condition de Fermat
            continue # Cette base ne convient pas, on ne peut pas conclure pour n avec elle

        # Vérification de la condition forte de Lucas
        is_suitable_base = True
        for q_factor in prime_factors_phi:
            if pow_mod(base, phi // q_factor, n) == 1:
                is_suitable_base = False
                break
        if is_suitable_base:
            return True # n est premier si on trouve une telle base
    return False # Si aucune base testée ne fonctionne



def test_pocklington(h,u,n):
    bases=[2,3,5,7,11,13,17,19,23,29]
    for base in bases:
        if pow_mod(base, (n - 1) // 2, n) == n-1 :
            return True
    print("On n'a pas trouvé de base qui verifie que n est premier. On ne peut pas conclure.")
    return False