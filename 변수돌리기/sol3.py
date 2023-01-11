list1 = [1, 'b', 3]
list2 = ['a', 2, 'b']

list1[1], list2[1] = list1[2], list2[1]

print(list1)
print(list2)