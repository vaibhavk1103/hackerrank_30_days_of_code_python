import sys


s = input().strip()
try:
    str = int(s)
    print(str)
except ValueError:
    print('Bad String')