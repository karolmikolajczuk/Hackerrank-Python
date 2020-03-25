#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix)
string = ""
for i in range(m):
    string += ''.join(char[i] for char in matrix)

print(string)

pattern = r'[!,@#$%&]{2}'

print(re.sub('(?<=\w)([!,@#$%& ]{2})(?=\w)', " ", string))
