member = [
    'Ada', 
    'Tovalds', 
    'Turing',
]

long_name = ''
len_name = 0
for m in member:
    if len(m)> len_name:
        long_name = m
        len_name = len(m)
print(long_name)