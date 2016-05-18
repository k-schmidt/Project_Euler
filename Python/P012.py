from itertools import count

def generate_triangle_number():
    sum = 0
    for i in count(1):
        sum += i
        print(sum)
        yield sum

def generate_prime_factors(number):
    prime = 2
    factors = {1, number}
    
    while prime**2 <= number:
        if number % prime == 0:
            another_factor = number // prime
            factors.add(another_factor)
            factors.add(prime)
        prime += 1
    print(factors)
    return len(factors)

def problem_runner():
    for i in generate_triangle_number():
        print(i)
        count = generate_prime_factors(i)
        print(count)
        if count >= 500:
            return i
    return "Not found"

if __name__ == "__main__":
    print(problem_runner())
