"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer.")

    prime_list = []
    current_number = 2

    while len(prime_list) < number_of_primes:
        is_prime = all(current_number % prime != 0 for prime in prime_list)
        if is_prime:
            prime_list.append(current_number)
        current_number += 1

    return prime_list
