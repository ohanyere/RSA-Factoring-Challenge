#!/usr/bin/python3
'''Handles the generation of 2 factors for a given number'''
import sys


def factorize(num):
    '''Method that generates 2 factors for a given number'''
    fact1 = 2
    while (num % fact1):
        if (fact1 <= num):
            fact1 += 1

    fact2 = num // fact1
    return (fact2, fact1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    fact2, fact1 = factorize(num)
    print(f"{num} = {fact2} * {fact1}")
