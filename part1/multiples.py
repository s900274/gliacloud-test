# -*- coding: utf-8 -*-

def sumOfMultiples(param):
    sum = 0
    for count in range(param):
        if (count % 3 ==0) or (count % 5 == 0):
            sum += count
    return sum

print(sumOfMultiples(100))