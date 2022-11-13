import timeit

def execute_list_for(number: int):
    result = []
    for n in range(number):
        result.append(n * 2)
    return result


def execute_list_comprehension(number: int):
    return [n * 2 for n in range(number)]


# TEST CASE2 : 길이 10000 를 총 10000번 돌렸을 때 시간
for case in range(10):
    t1 = timeit.timeit(lambda: execute_list_for(10000), number=10000)  # default_number = 1000000
    t2 = timeit.timeit(lambda: execute_list_comprehension(10000), number=10000)
    print(f'[TEST{case}] : {(t1-t2)/t2*100:0.2f}% {t1,t2}')