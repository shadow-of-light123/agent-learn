def find_primes_up_to_n(n: int) -> list[int]:
    """Return all prime numbers from 2 to n (inclusive).

    Uses Euler's linear sieve (O(n) time) to ensure each composite number
    is crossed out exactly once by its smallest prime factor.

    Args:
        n: An integer upper bound (inclusive).

    Returns:
        A list of prime numbers in ascending order.  If n < 2, an empty
        list is returned.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    primes: list[int] = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

        # Cross out multiples using the smallest prime factor
        for p in primes:
            multiple = i * p
            if multiple > n:
                break
            is_prime[multiple] = False
            if i % p == 0:
                break

    return primes

if __name__ == "__main__":
    primes = find_primes_up_to_n(1100)
    print(primes)