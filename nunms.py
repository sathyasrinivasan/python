import sys
sys.getrefcount(1)

a=3
b=a
# BUG:
print(b)

a = 4
b = 5
print (b)
print(a)
