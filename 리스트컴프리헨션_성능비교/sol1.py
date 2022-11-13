import timeit

def execute_list_for(number: int):
    result = []
    for n in range(number):
        result.append(n * 2)
    return result


def execute_list_comprehension(number: int):
    return [n * 2 for n in range(number)]


# TEST CASE1 : 리스트 길이가 5 ~ 50 일 때
win_list_for = 0
win_list_comprehension = 0
for case in range(5, 50):
    t1 = timeit.timeit(lambda: execute_list_for(case), number=1)  # default_number = 1000000
    t2 = timeit.timeit(lambda: execute_list_comprehension(case), number=1)
    if t1 < t2:
        win_list_for += 1
    elif t2 < t1:
        win_list_comprehension += 1
    print(f'[{case=}]{win_list_for = } {win_list_comprehension = }')