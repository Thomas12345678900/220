"""
Name: Thomas Scola
hw10.py
Problem: completing assignments that work will loops and booleans
Certification of Authenticity:
I received help from the CSL with Brooke Duvall.
"""

def fibonacci(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def double_investment(principle, rate):
    annual = 0
    count = 0
    while annual != principle * 2:
        annual = float(principle) * (1 + float(rate))
        count += 1
        principle = annual
    return principle

def syracuse(num):
    print(str(num) + ", ", end=" ")
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1

        if num != 1:
            print(str(num)+ ", ", end="")
        else:
            print(1)

def goldbach(n):
    #prime numbers "function"
    prime_numbers = []

    value = 1
    while value <= n:
        counter = 0
        integer = 2
        while integer <= value//2:
            if value % integer == 0:
                counter = counter + 1
                break
            integer = integer + 1
        if counter == 0 and value != 1:
            prime_numbers.append(value)
        value = value + 1

    if n % 2 != 0:
        return None

    index_prime_num1 = 0
    index_prime_num2 = 0

    prime_number_1 = prime_numbers[index_prime_num1]
    prime_number_2 = prime_numbers[index_prime_num2]

    while prime_number_1 + prime_number_2 != n:
        if prime_number_2 == prime_numbers[-1]:
            index_prime_num1 = index_prime_num1 + 1
            index_prime_num2 = index_prime_num2 + 1
            prime_number_1 = prime_numbers[index_prime_num1]
            prime_number_2 = prime_numbers[index_prime_num2]
        else:
            index_prime_num2 = index_prime_num2 + 1
            prime_number_2 = prime_numbers[index_prime_num2]
    return [prime_number_1, prime_number_2]


if __name__ == '__main__':
    pass
