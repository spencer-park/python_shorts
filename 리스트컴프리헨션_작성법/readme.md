## 리스트컴프리헨션 어렵지 않아요.
파이썬 for문을 작성하실 줄 안다면, 1분만에 리스트컴프리헨션 할 수 있습니다.

## for문의 특정 상황 -> 리스트 컴프리헨션
for문은 리스트와 같이 유한한 n개의 데이터가 있을 때 각 값을 참고하여 기능 수행할 때 유용합니다.
그런데 수행할 기능이 `list.append(val)` 처럼 또 리스트를 만드는 것이라면 list_comprehension을 쓰는 게 좋습니다.

1. for문을 사용하는데
1. 처리하는 데이터로 기존/새로운 리스트에 `.append(val)`한다면
1. list comprehension


## 작성 과정 확인
참고 : sol1.py
```python
numbers = [1, 2, 3, 4, 5, 6]

# 특정 상황 : 반복해서 처리한 값들을 새로운 곳에 담는다
results1 = []
for n in numbers:
    results1.append(n * 2)
print(results1)

# 리스트 컴프리헨션
# 1. 리스트 안에 for 문을 : 이전까지 적는다.
# 2. 앞에 무엇을 남길지 적는다.
results2 = [n*2 for n in numbers]
print(results2)
```

## 꼭 리스트와 관련없는 데이터를 남겨도 된다.
'반드시 for문에 사용된 데이터를 활용해야한다' 는 생각에 막히는 경우가 있습니다. 꼭 그럴필요는 없습니다.
참고 : sol2.py
```python
member = ['스펜서', '숲헨서', '수붼서']
score_table1 = []
for _ in member:
    score_table1.append(0)
print(score_table1)

# list comprehension
score_table2 = [0 for _ in member]
print(score_table2)
```