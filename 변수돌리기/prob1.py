a = 1
b = 2
print(a, b)

# b <-> a
c = a
a = b
b = c
del c
print(a, b)