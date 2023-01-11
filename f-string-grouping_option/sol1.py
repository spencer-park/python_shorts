money = 10000000
money = 10_000_000
print(money)

# https://docs.python.org/3/library/string.html#format-string-syntax
# https://docs.python.org/3/library/string.html#format-specification-mini-language
# f'{<expr>:<format_spec>}'
print(f'{money:{"_"}d}')
print(f'{money:{","}d}')
