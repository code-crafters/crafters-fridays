#!/bin/python3
import resource
from sys import argv

DIGITAL_BASE = 10
# to improve code: https://www.hackerrank.com/challenges/find-digits/topics/div-mod
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
    
def selectFunction():
    if len(argv) < 2:
        function_ = 1
    else:
        function_ = int(argv[1])
    if function_ == 1:
        print("Elegiste: numero a str")
    else:
        print("Elegiste: dividir numero")
    return function_
if __name__ == '__main__':
    function_ = selectFunction()
    print("Memoria:",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    n_ = [12, 1012, 101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268101248881044010102681012488810440101026810124888104401010268]

    for n in n_:
        if function_ == 1:
            result = findDigits(n)
        elif function_ == 2:
            result = findDigitsDigitalBase(n)
        print("Resultado",result)

"""
La libreria 'resource' es para comparar entre findDigits y findDigitsDigitalBase.
Donde la primera transforma un entero a una lista de enteros y el segundo hace 
divisiones del numero para obtener sus digitos.

En las pruebas, se utilizo la lista n_
En el primer caso:
Memoria: 9160
Resultado 2
Resultado 3
Resultado 627

real    0m0.039s
user    0m0.032s
sys 0m0.004s

El resultado de findDigitsDigitalBase:
Memoria: 9172
Resultado 2
Resultado 3
Resultado 760

real    0m0.039s
user    0m0.040s
sys 0m0.000s

"""