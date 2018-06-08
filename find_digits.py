#!/bin/python3

def findDigits(n):
    numbers = str(n)
    count = 0
    for number in numbers:
        if int(number) != 0 and n % int(number) == 0:
            count += 1
    return count
    
if __name__ == '__main__':
    t = int(input("Numero de casos de prueba: "))
    for t_itr in range(t):
        n = int(input("> "))
        result = findDigits(n)
        print(result)
