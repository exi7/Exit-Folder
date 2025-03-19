def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

if __name__ == "__main__":
    limit = int(input("Enter a limit: "))
    primes = prime_numbers(limit)
    print(f"Prime numbers from 2 to {limit} are: {', '.join(map(str, primes))}")
