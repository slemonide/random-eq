#!/usr/bin/env python3
import random
import math

numbers = [x + 1 for x in range(9)]

count = 1
while True:
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    answer = str(num1 + num2)
    equation = str(num1) + ' + ' + str(num2) + ' = '
    read = input(equation)

    if read == answer:
        print(count)
        count = count + 1

    if count == 11:
        break
