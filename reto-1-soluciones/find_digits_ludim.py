#!/bin/python3
DIGITAL_BASE = 10

# To improve code: https://www.hackerrank.com/challenges/find-digits/topics/div-mod
def findDigitsDigitalBase(n):
    count = 0
    while (n != 0):
        number = n % DIGITAL_BASE
        if number != 0 and n % number == 0: count += 1
        n //= 10
    return count

def findDigits(n):
    numbers = str(n)
    count = 0
    for number in numbers:
        if int(number) != 0 and n % int(number) == 0: count += 1
    return count
    
if __name__ == '__main__':
    t = int(input("Numero de casos de prueba: "))
    for t_itr in range(t):
        n = int(input("> "))
        result = findDigits(n)
        result = findDigitsDigitalBase(n)
        print(result)