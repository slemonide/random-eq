#!/usr/bin/env python3
import random
import math
from time import time

numbers = range(1, 10)

count = 1
t_0 = time()
while True:
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    answer = str(num1 + num2)
    equation = str(num1) + ' + ' + str(num2) + ' = '
    read = input(equation)

    if read == answer:
        print(count)
        count += 1

    if count == len(numbers) + 1:
        break

t = time()
t_delta = t - t_0
mind_power = len(numbers) / t_delta * (10 ** 3) #(10 ** 3) represents "milli-"
print('Your mind power: ' + str(mind_power) + '1/ms')
