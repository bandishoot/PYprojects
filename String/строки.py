from math import *

s = input()
print(s[ceil(len(s)/2):] + s[:ceil(len(s)/2)])
