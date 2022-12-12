def double(x):
    return 2 * x

def execute_list_map(n_list: list):
    return list(map(double, n_list))


def execute_list_comprehension(n_list: list):
    return [double(n) for n in n_list]


# TEST CASE2 : 길이 10000 를 총 10000번 돌렸을 때 시간
n_list = list(range(10000))
print(execute_list_map(n_list)[0])
print(execute_list_comprehension(n_list)[0])
print(execute_list_map(n_list) == execute_list_comprehension(n_list))