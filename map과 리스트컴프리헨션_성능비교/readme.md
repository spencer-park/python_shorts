## 리스트 컴프리헨션 꼭 써야돼?
꼭 이란 건 없지만, 내가 성능을 조금이라도 올리고자 한다면 쓰자! 왜 그런지는 성능을 확인해보며 확인해보자.
테스트 환경은 다음과 같다.
- MacBook Pro 
    - 프로세서 : 1.4 GHz 쿼드 코어 Intel Core i5
    - 메모리 : 8GB 2133 MHz LPDDR3
    - 그래픽 : Intel Iris Plus Graphics 645 1536 MB
- Python 3.10.4 64-bit

## 테스트 1 : 데이터의 길이가 5~50개일 때
참고 : sol1.py
```python
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
```
리스트컴프리헨션이 전부 이기거나
초반 구간에는 전부 이기다가 중간에 간혹 지는 곳이 있다.
그런데 5~50이나 컴퓨터 입장에선 개수가 적은 경우다.

## 테스트 2 : 성능계산율 계산
참고 : sol2.py
```python
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
```
10000개의 데이터를 처리하는 것을 10000번 실행했을 때의 총 시간을 계산하여, 성능계산이 얼마나 이루어졌는지 확인해보도록 하자.
`성능계산율(%) = (기존시간 - 개선시간) / 개선시간 * 100`

테스트까지 꽤 시간이 걸리며 10번 정도 테스트한 성능개선율은 다음과 같았다.
```
[TEST0] : 60.92% (8.936443001992302, 5.553426450002007)
[TEST1] : 56.40% (8.535639841997181, 5.457505726997624)
[TEST2] : 54.47% (8.672129063998, 5.613950044993544)
[TEST3] : 55.81% (8.733219513000222, 5.605085317991325)
[TEST4] : 59.20% (8.4348543209926, 5.298438565005199)
[TEST5] : 50.70% (8.265676184004406, 5.484998471001745)
[TEST6] : 54.98% (8.582092677999754, 5.537443855995662)
[TEST7] : 57.17% (8.886132408995763, 5.653859058002126)
[TEST8] : 56.78% (8.735787918994902, 5.572083327002474)
[TEST9] : 54.79% (8.594605776990647, 5.552603173011448)
```