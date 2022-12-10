import timeit

def double(x):
    return 2 * x

def execute_list_map(n_list: list):
    return list(map(double, n_list))


def execute_list_comprehension(n_list: list):
    return [double(n) for n in n_list]


# TEST CASE2 : 길이 10000 를 총 10000번 돌렸을 때 시간
for case in range(10):
    n_list = list(range(10000))
    t1 = timeit.timeit(lambda: execute_list_map(n_list), number=10000)  # default_number = 1000000
    t2 = timeit.timeit(lambda: execute_list_comprehension(n_list), number=10000)
    print(f'[TEST{case}] : {(t1-t2)/t2*100:0.2f}% {t1,t2}')